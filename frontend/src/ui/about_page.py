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
