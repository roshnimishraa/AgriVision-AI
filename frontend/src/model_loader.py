"""
All model/artifact loading lives here. Two design choices here specifically target
the "app feels slow" complaint:

1. Each model is its OWN cached function, not one load_all() bundle. A tab that only
   needs the end-to-end yield model doesn't drag in the (much larger) baseline and
   oracle models too. Callers should only call the loader for the model they're
   actually about to use, and ideally only inside the button-click / upload branch
   -- not unconditionally at the top of a tab's render().

2. The Random Forest joblib files are loaded with mmap_mode="r", so scikit-learn
   memory-maps the underlying numpy arrays from disk instead of deserializing the
   full ~370MB+ object into RAM upfront. This matters a lot on a memory-limited
   deployment (e.g. Streamlit Community Cloud's free tier).

Cheap existence checks (os.path.exists) are separated out from the actual loaders so
a tab can decide what UI to show (e.g. "not available") without paying the loading
cost just to render a warning message.
"""

import os
import joblib
import streamlit as st

from src import config


# ------------------------------------------------------------------
# Cheap existence checks -- use these for UI decisions, NOT the loaders below
# ------------------------------------------------------------------
def disease_model_available():
    return os.path.exists(config.DISEASE_MODEL_PATH) and os.path.exists(config.DISEASE_META_PATH)


def encoders_available():
    return os.path.exists(config.FUSION_ENCODERS_PATH) or (
        os.path.exists(config.AREA_ENCODER_PATH) and os.path.exists(config.ITEM_ENCODER_PATH)
    )


def endtoend_model_available():
    return os.path.exists(config.YIELD_MODEL_ENDTOEND_PATH)


def baseline_model_available():
    return os.path.exists(config.YIELD_MODEL_BASELINE_PATH)


def oracle_model_available():
    return os.path.exists(config.YIELD_MODEL_ORACLE_PATH)


# ------------------------------------------------------------------
# Actual loaders -- each cached independently. Call these lazily, at the point
# you're about to use the model (e.g. inside `if uploaded:` or `if st.button(...)`),
# not unconditionally every time a tab renders.
# ------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def load_disease_model():
    if not disease_model_available():
        return None
    import tensorflow as tf
    return tf.keras.models.load_model(config.DISEASE_MODEL_PATH)


@st.cache_resource(show_spinner=False)
def load_disease_meta():
    if not os.path.exists(config.DISEASE_META_PATH):
        return None
    return joblib.load(config.DISEASE_META_PATH)


@st.cache_resource(show_spinner=False)
def load_encoders():
    if os.path.exists(config.FUSION_ENCODERS_PATH):
        return joblib.load(config.FUSION_ENCODERS_PATH)
    if os.path.exists(config.AREA_ENCODER_PATH) and os.path.exists(config.ITEM_ENCODER_PATH):
        return {
            "area_encoder": joblib.load(config.AREA_ENCODER_PATH),
            "item_encoder": joblib.load(config.ITEM_ENCODER_PATH),
        }
    return None


@st.cache_resource(show_spinner=False)
def load_endtoend_yield_model():
    if not endtoend_model_available():
        return None
    return joblib.load(config.YIELD_MODEL_ENDTOEND_PATH, mmap_mode="r")


@st.cache_resource(show_spinner=False)
def load_baseline_yield_model():
    if not baseline_model_available():
        return None
    return joblib.load(config.YIELD_MODEL_BASELINE_PATH, mmap_mode="r")


@st.cache_resource(show_spinner=False)
def load_oracle_yield_model():
    if not oracle_model_available():
        return None
    return joblib.load(config.YIELD_MODEL_ORACLE_PATH, mmap_mode="r")
