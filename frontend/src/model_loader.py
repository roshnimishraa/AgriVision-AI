import os
import joblib
import streamlit as st

from huggingface_hub import hf_hub_download

from src import config


def download_hf_model(filename):
    return hf_hub_download(
        repo_id=config.HF_MODEL_REPO,
        filename=filename,
        cache_dir=config.HF_CACHE_DIR
    )


def disease_model_available():
    return (
        os.path.exists(config.DISEASE_MODEL_PATH)
        or _hf_exists(config.DISEASE_MODEL_FILENAME)
    ) and (
        os.path.exists(config.DISEASE_META_PATH)
        or _hf_exists(config.DISEASE_META_FILENAME)
    )


def encoders_available():
    if os.path.exists(config.FUSION_ENCODERS_PATH):
        return True

    if (
        os.path.exists(config.AREA_ENCODER_PATH)
        and os.path.exists(config.ITEM_ENCODER_PATH)
    ):
        return True

    return _hf_exists(config.FUSION_ENCODERS_FILENAME)


def endtoend_model_available():
    return (
        os.path.exists(config.YIELD_MODEL_ENDTOEND_PATH)
        or _hf_exists(config.YIELD_MODEL_ENDTOEND_FILENAME)
    )


def baseline_model_available():
    return (
        os.path.exists(config.YIELD_MODEL_BASELINE_PATH)
        or _hf_exists(config.YIELD_MODEL_BASELINE_FILENAME)
    )


def oracle_model_available():
    return (
        os.path.exists(config.YIELD_MODEL_ORACLE_PATH)
        or _hf_exists(config.YIELD_MODEL_ORACLE_FILENAME)
    )


def _hf_exists(filename):
    try:
        download_hf_model(filename)
        return True
    except Exception:
        return False


@st.cache_resource(show_spinner=False)
def load_disease_model():

    path = config.DISEASE_MODEL_PATH

    if not os.path.exists(path):
        path = download_hf_model(
            config.DISEASE_MODEL_FILENAME
        )

    import tensorflow as tf

    return tf.keras.models.load_model(path)


@st.cache_resource(show_spinner=False)
def load_disease_meta():

    path = config.DISEASE_META_PATH

    if not os.path.exists(path):
        path = download_hf_model(
            config.DISEASE_META_FILENAME
        )

    return joblib.load(path)


@st.cache_resource(show_spinner=False)
def load_encoders():

    if os.path.exists(config.FUSION_ENCODERS_PATH):
        return joblib.load(
            config.FUSION_ENCODERS_PATH
        )

    if (
        os.path.exists(config.AREA_ENCODER_PATH)
        and os.path.exists(config.ITEM_ENCODER_PATH)
    ):
        return {
            "area_encoder": joblib.load(
                config.AREA_ENCODER_PATH
            ),
            "item_encoder": joblib.load(
                config.ITEM_ENCODER_PATH
            ),
        }

    path = download_hf_model(
        config.FUSION_ENCODERS_FILENAME
    )

    return joblib.load(path)


@st.cache_resource(show_spinner=False)
def load_endtoend_yield_model():

    path = config.YIELD_MODEL_ENDTOEND_PATH

    if not os.path.exists(path):
        path = download_hf_model(
            config.YIELD_MODEL_ENDTOEND_FILENAME
        )

    return joblib.load(
        path,
        mmap_mode="r"
    )


@st.cache_resource(show_spinner=False)
def load_baseline_yield_model():

    path = config.YIELD_MODEL_BASELINE_PATH

    if not os.path.exists(path):
        path = download_hf_model(
            config.YIELD_MODEL_BASELINE_FILENAME
        )

    return joblib.load(
        path,
        mmap_mode="r"
    )


@st.cache_resource(show_spinner=False)
def load_oracle_yield_model():

    path = config.YIELD_MODEL_ORACLE_PATH

    if not os.path.exists(path):
        path = download_hf_model(
            config.YIELD_MODEL_ORACLE_FILENAME
        )

    return joblib.load(
        path,
        mmap_mode="r"
    )
