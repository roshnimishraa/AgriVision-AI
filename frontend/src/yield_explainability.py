"""
Live SHAP explanation for the yield model. Unlike static exported PNGs, this computes
a real explanation for the SPECIFIC prediction just made, using shap.TreeExplainer --
which is exact and fast for Random Forests, with no background dataset needed.

This is what makes the yield side of the project actually "explainable" the same way
Grad-CAM makes the disease side explainable: both explain the one prediction just shown
to the user, not a generic dataset-level plot.
"""

import streamlit as st
import matplotlib.pyplot as plt

from src import model_loader


@st.cache_resource(show_spinner=False)
def get_endtoend_explainer():
    """Builds the SHAP explainer once for the end-to-end fused yield model."""
    import shap
    model = model_loader.load_endtoend_yield_model()
    if model is None:
        return None
    return shap.TreeExplainer(model)


def explain_prediction(row_df, feature_cols):
    """Returns a matplotlib figure explaining ONE specific prediction (the row just
    predicted), or None if the explainer isn't available. Caller must plt.close(fig)
    after displaying it to avoid memory buildup across reruns."""
    explainer = get_endtoend_explainer()
    if explainer is None:
        return None

    import shap
    shap_values = explainer(row_df[feature_cols])

    fig = plt.figure(figsize=(7, 4))
    shap.plots.waterfall(shap_values[0], show=False)
    plt.tight_layout()
    return fig
