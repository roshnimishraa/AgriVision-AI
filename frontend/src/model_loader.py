import os
import joblib
import streamlit as st

from src import config


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

    return joblib.load(
        config.YIELD_MODEL_ENDTOEND_PATH,
        mmap_mode="r"
    )


@st.cache_resource(show_spinner=False)
def load_baseline_yield_model():
    if not baseline_model_available():
        return None

    return joblib.load(
        config.YIELD_MODEL_BASELINE_PATH,
        mmap_mode="r"
    )


@st.cache_resource(show_spinner=False)
def load_oracle_yield_model():
    if not oracle_model_available():
        return None

    return joblib.load(
        config.YIELD_MODEL_ORACLE_PATH,
        mmap_mode="r"
    )
    
