"""
Yield prediction: turns raw form inputs + a disease severity value into a
feature row and runs it through whichever RF model you pass in.

IMPORTANT: your three yield models were trained on three DIFFERENT feature sets:
    - baseline_yield_model.joblib          -> BASE_FEATURES only, no severity column
    - fused_yield_model_endtoend.joblib     -> BASE_FEATURES + "disease_severity_endtoend"
    - fused_yield_model_oracle.joblib       -> BASE_FEATURES + "disease_severity_oracle"

Passing the wrong column name/set raises a scikit-learn "feature names should match
those passed during fit" error, so every call to predict() must pass the matching
`severity_feature_name` (or None for the baseline model).
"""

import pandas as pd

from src import config


def build_feature_row(encoders, area, item, year, rainfall, pesticides, temp,
                       severity=None, severity_feature_name=None):
    """Encodes categorical fields and assembles the feature row.
    Only includes a severity column at all if severity_feature_name is given."""
    le_area, le_item = encoders["area_encoder"], encoders["item_encoder"]

    try:
        area_enc = int(le_area.transform([area])[0])
    except ValueError:
        area_enc = 0  # unseen label fallback

    try:
        item_enc = int(le_item.transform([item])[0])
    except ValueError:
        item_enc = 0

    row = {
        "Area_enc": area_enc,
        "Item_enc": item_enc,
        "Year": year,
        "average_rain_fall_mm_per_year": rainfall,
        "pesticides_tonnes": pesticides,
        "avg_temp": temp,
    }
    if severity_feature_name is not None:
        row[severity_feature_name] = severity

    return pd.DataFrame([row])


def supported_yield_items(all_items):
    """Filters the yield dataset's crop list down to only the crops the disease
    model actually recognizes, so the Full Pipeline tab can't combine a detected
    disease on one crop with a yield forecast for an unrelated crop.

    Uses an EXACT match (not substring) -- a substring check would incorrectly
    match e.g. "Sweet potatoes" against "potato"."""
    all_accepted = set()
    for names in config.CROP_EXACT_MATCHES.values():
        all_accepted |= names
    matches = [item for item in all_items if str(item).strip().lower() in all_accepted]
    return sorted(matches)


def yield_item_for_disease_class(disease_class, all_items):
    """Given a detected disease class name (e.g. 'Potato___Late_blight'), finds the
    best-matching crop name in the yield dataset's Item list. Returns None if no match."""
    disease_lower = disease_class.lower()
    for disease_kw, accepted_names in config.CROP_EXACT_MATCHES.items():
        if disease_kw in disease_lower:
            for item in all_items:
                if str(item).strip().lower() in accepted_names:
                    return item
    return None



def predict(model, encoders, area, item, year, rainfall, pesticides, temp,
            severity=None, severity_feature_name=None):
    """Runs a single yield prediction.

    `severity_feature_name` MUST match how the specific `model` you're calling was trained:
        - baseline model  -> pass None (no severity feature at all)
        - end-to-end model -> pass config.SEVERITY_FEATURE_ENDTOEND
        - oracle model     -> pass config.SEVERITY_FEATURE_ORACLE
    """
    pred, _row, _cols = predict_with_row(model, encoders, area, item, year, rainfall,
                                          pesticides, temp, severity, severity_feature_name)
    return pred


def predict_with_row(model, encoders, area, item, year, rainfall, pesticides, temp,
                      severity=None, severity_feature_name=None):
    """Same as predict(), but also returns (row_df, feature_cols) -- needed by
    src/yield_explainability.py to compute a SHAP explanation for this exact prediction."""
    row = build_feature_row(encoders, area, item, year, rainfall, pesticides, temp,
                             severity, severity_feature_name)
    feature_cols = list(config.BASE_FEATURES)
    if severity_feature_name is not None:
        feature_cols.append(severity_feature_name)
    pred = float(model.predict(row[feature_cols])[0])
    return pred, row, feature_cols
