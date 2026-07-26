import streamlit as st
from src.ui import theme
from src.ui.html_utils import render_html


def render():

    theme.about_hero(
        "About AgriVision AI",
        "AgriVision AI is an explainable multimodal agricultural intelligence platform that "
        "combines deep learning and machine learning to detect crop diseases and predict crop "
        "yield within a single integrated system. By analyzing crop leaf images alongside "
        "environmental and agricultural parameters, the platform provides reliable predictions "
        "supported by transparent AI explanations to help farmers, researchers, and students "
        "make informed agricultural decisions."
    )

    
#     st.markdown("## Why AgriVision AI?")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown(
#             """
# ### Disease Detection

# Detects diseases from crop leaf images using an EfficientNetB0
# deep learning model and predicts the disease class along with
# its confidence score.
# """
#         )

#     with col2:
#         st.markdown(
#             """
# ### Yield Prediction

# Predicts crop yield using a Random Forest model trained on
# environmental and agricultural parameters such as rainfall,
# temperature, pesticide usage, crop type and cultivation area.
# """
#         )

#     st.markdown("## Problem Statement")

#     st.write(
#         """
# Agricultural productivity is significantly affected by crop diseases,
# climate conditions, and farming practices. Most existing solutions
# focus either on disease detection or yield prediction independently,
# making it difficult to understand how crop health influences
# agricultural productivity.

# AgriVision AI addresses this challenge by integrating both tasks into
# a unified explainable system, enabling users to assess crop health,
# estimate crop yield, and understand the reasoning behind every
# prediction through Explainable AI techniques.
# """
#     )

#     st.markdown("## Key Features")

#     c1, c2 = st.columns(2)

#     with c1:
#         st.markdown(
#             """
# ### Disease Analysis

# ✔ Upload crop leaf images

# ✔ Detect diseases automatically

# ✔ Confidence score prediction

# ✔ Disease severity estimation

# ✔ Grad-CAM visual explanation
# """
#         )

#     with c2:
#         st.markdown(
#             """
# ### Yield Analysis

# ✔ Crop yield prediction

# ✔ Uses rainfall & temperature

# ✔ Includes pesticide usage

# ✔ Supports multiple crops & regions

# ✔ SHAP feature explanation
# """
#         )

#     st.markdown("## What Makes AgriVision AI Different?")

#     st.markdown(
#         """
# Unlike conventional agricultural applications that perform only a
# single task, AgriVision AI combines **Computer Vision**, **Machine
# Learning**, and **Explainable AI** into one intelligent platform.
# This enables users to understand not only *what* the prediction is,
# but also *why* the model made that prediction.
# """
#     )