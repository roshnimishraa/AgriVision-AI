import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


ASSETS_DIR = os.path.join(
    BASE_DIR,
    "assets"
)


HF_MODEL_REPO = "roshni-mishra/agrivision-models"

HF_CACHE_DIR = os.path.join(
    BASE_DIR,
    "hf_models"
)


# -------------------------
# Disease Model
# -------------------------

DISEASE_MODEL_FILENAME = "best_disease_model.keras"
DISEASE_META_FILENAME = "disease_meta.joblib"


DISEASE_MODEL_PATH = os.path.join(
    HF_CACHE_DIR,
    DISEASE_MODEL_FILENAME
)


DISEASE_META_PATH = os.path.join(
    HF_CACHE_DIR,
    DISEASE_META_FILENAME
)


IMG_SIZE_CNN = 224



# -------------------------
# Encoders
# -------------------------

FUSION_ENCODERS_FILENAME = "fusion_encoders.joblib"
AREA_ENCODER_FILENAME = "area_encoder.pkl"
ITEM_ENCODER_FILENAME = "item_encoder.pkl"


FUSION_ENCODERS_PATH = os.path.join(
    HF_CACHE_DIR,
    FUSION_ENCODERS_FILENAME
)


AREA_ENCODER_PATH = os.path.join(
    HF_CACHE_DIR,
    AREA_ENCODER_FILENAME
)


ITEM_ENCODER_PATH = os.path.join(
    HF_CACHE_DIR,
    ITEM_ENCODER_FILENAME
)



# -------------------------
# Yield Models
# -------------------------

YIELD_MODEL_ENDTOEND_FILENAME = "fused_yield_model_endtoend.joblib"
YIELD_MODEL_ORACLE_FILENAME = "fused_yield_model_oracle.joblib"
YIELD_MODEL_BASELINE_FILENAME = "baseline_yield_model.joblib"


YIELD_MODEL_ENDTOEND_PATH = os.path.join(
    HF_CACHE_DIR,
    YIELD_MODEL_ENDTOEND_FILENAME
)


YIELD_MODEL_ORACLE_PATH = os.path.join(
    HF_CACHE_DIR,
    YIELD_MODEL_ORACLE_FILENAME
)


YIELD_MODEL_BASELINE_PATH = os.path.join(
    HF_CACHE_DIR,
    YIELD_MODEL_BASELINE_FILENAME
)



# -------------------------
# Features
# -------------------------

BASE_FEATURES = [
    "Area_enc",
    "Item_enc",
    "Year",
    "average_rain_fall_mm_per_year",
    "pesticides_tonnes",
    "avg_temp",
]


SEVERITY_FEATURE_ENDTOEND = "disease_severity_endtoend"
SEVERITY_FEATURE_ORACLE = "disease_severity_oracle"



# -------------------------
# Crop Matching
# -------------------------

CROP_EXACT_MATCHES = {
    "potato": {
        "potato",
        "potatoes"
    },
    "corn": {
        "maize",
        "corn"
    },
    "soybean": {
        "soybean",
        "soybeans"
    },
}



# -------------------------
# Assets
# -------------------------

SAMPLE_LEAF_PATH = os.path.join(
    ASSETS_DIR,
    "sample_images",
    "sample_leaf.jpg"
)


HERO_IMAGE_PATH = os.path.join(
    ASSETS_DIR,
    "hero.jpg"
)



# -------------------------
# Disease Figures
# -------------------------

DISEASE_FIGURES_DIR = os.path.join(
    ASSETS_DIR,
    "disease_figures"
)


DISEASE_CONFUSION_MATRIX_PATH = os.path.join(
    DISEASE_FIGURES_DIR,
    "disease_confusion_matrix.png"
)


DISEASE_GRADCAM_SAMPLE_PATH = os.path.join(
    DISEASE_FIGURES_DIR,
    "disease_gradcam.png"
)


DISEASE_OCCLUSION_SALIENCY_PATH = os.path.join(
    DISEASE_FIGURES_DIR,
    "disease_occlusion_saliency.png"
)


DISEASE_SHAP_FEATURE_IMPORTANCE_PATH = os.path.join(
    DISEASE_FIGURES_DIR,
    "disease_shap_feature_importance.png"
)



# -------------------------
# Yield Figures
# -------------------------

YIELD_FIGURES_DIR = os.path.join(
    ASSETS_DIR,
    "yield_figures"
)


YIELD_SHAP_BAR_PATH = os.path.join(
    YIELD_FIGURES_DIR,
    "SHAP_Bar.png"
)


YIELD_SHAP_BEESWARM_PATH = os.path.join(
    YIELD_FIGURES_DIR,
    "SHAP_Beeswarm.png"
)


YIELD_SHAP_WATERFALL_PATH = os.path.join(
    YIELD_FIGURES_DIR,
    "SHAP_Waterfall.png"
)


YIELD_FUSION_COMPARISON_PATH = os.path.join(
    YIELD_FIGURES_DIR,
    "fusion_comparison.png"
)
