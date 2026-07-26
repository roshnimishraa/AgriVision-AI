import pandas as pd

from src import config


def build_feature_row(
    encoders,
    area,
    item,
    year,
    rainfall,
    pesticides,
    temp,
    severity=None,
    severity_feature_name=None,
):

    le_area = encoders["area_encoder"]
    le_item = encoders["item_encoder"]

    try:
        area_enc = int(le_area.transform([area])[0])
    except ValueError:
        area_enc = 0

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
    all_accepted = set()

    for names in config.CROP_EXACT_MATCHES.values():
        all_accepted |= names

    matches = [
        item
        for item in all_items
        if str(item).strip().lower() in all_accepted
    ]

    return sorted(matches)


def yield_item_for_disease_class(disease_class, all_items):
    disease_lower = disease_class.lower()

    for disease_kw, accepted_names in config.CROP_EXACT_MATCHES.items():
        if disease_kw in disease_lower:
            for item in all_items:
                if str(item).strip().lower() in accepted_names:
                    return item

    return None


def predict(
    model,
    encoders,
    area,
    item,
    year,
    rainfall,
    pesticides,
    temp,
    severity=None,
    severity_feature_name=None,
):

    pred, _, _ = predict_with_row(
        model,
        encoders,
        area,
        item,
        year,
        rainfall,
        pesticides,
        temp,
        severity,
        severity_feature_name,
    )

    return pred


def predict_with_row(
    model,
    encoders,
    area,
    item,
    year,
    rainfall,
    pesticides,
    temp,
    severity=None,
    severity_feature_name=None,
):

    row = build_feature_row(
        encoders,
        area,
        item,
        year,
        rainfall,
        pesticides,
        temp,
        severity,
        severity_feature_name,
    )

    feature_cols = list(config.BASE_FEATURES)

    if severity_feature_name is not None:
        feature_cols.append(severity_feature_name)

    pred = float(model.predict(row[feature_cols])[0])

    return pred, row, feature_cols
