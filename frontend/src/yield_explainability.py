import streamlit as st
import matplotlib.pyplot as plt

from src import model_loader


@st.cache_resource(show_spinner=False)
def get_endtoend_explainer():
    import shap

    model = model_loader.load_endtoend_yield_model()

    if model is None:
        return None

    return shap.TreeExplainer(model)


def explain_prediction(row_df, feature_cols):
    explainer = get_endtoend_explainer()

    if explainer is None:
        return None

    import shap

    shap_values = explainer(row_df[feature_cols])

    fig = plt.figure(figsize=(7, 4))
    shap.plots.waterfall(shap_values[0], show=False)
    plt.tight_layout()

    return fig
