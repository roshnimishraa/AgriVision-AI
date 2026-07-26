import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

DISEASE_MODEL_PATH = os.path.join(MODELS_DIR, "best_disease_model.keras")
DISEASE_META_PATH = os.path.join(MODELS_DIR, "disease_meta.joblib")
IMG_SIZE_CNN = 224

FUSION_ENCODERS_PATH = os.path.join(MODELS_DIR, "fusion_encoders.joblib")
AREA_ENCODER_PATH = os.path.join(MODELS_DIR, "area_encoder.pkl")
ITEM_ENCODER_PATH = os.path.join(MODELS_DIR, "item_encoder.pkl")

YIELD_MODEL_ENDTOEND_PATH = os.path.join(MODELS_DIR, "fused_yield_model_endtoend.joblib")
YIELD_MODEL_ORACLE_PATH = os.path.join(MODELS_DIR, "fused_yield_model_oracle.joblib")
YIELD_MODEL_BASELINE_PATH = os.path.join(MODELS_DIR, "baseline_yield_model.joblib")

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

CROP_EXACT_MATCHES = {
    "potato": {"potato", "potatoes"},
    "corn": {"maize", "corn"},
    "soybean": {"soybean", "soybeans"},
}

ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SAMPLE_LEAF_PATH = os.path.join(ASSETS_DIR, "sample_images", "sample_leaf.jpg")
HERO_IMAGE_PATH = os.path.join(ASSETS_DIR, "hero.jpg")

DISEASE_FIGURES_DIR = os.path.join(ASSETS_DIR, "disease_detection_figures")
DISEASE_CONFUSION_MATRIX_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_confusion_matrix.png")
DISEASE_GRADCAM_SAMPLE_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_gradcam.png")
DISEASE_OCCLUSION_SALIENCY_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_occlusion_saliency.png")
DISEASE_SHAP_FEATURE_IMPORTANCE_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_shap_feature_importance.png")

YIELD_FIGURES_DIR = os.path.join(ASSETS_DIR, "yield_figures")
YIELD_SHAP_BAR_PATH = os.path.join(YIELD_FIGURES_DIR, "SHAP_Bar.png")
YIELD_SHAP_BEESWARM_PATH = os.path.join(YIELD_FIGURES_DIR, "SHAP_Beeswarm.png")
YIELD_SHAP_WATERFALL_PATH = os.path.join(YIELD_FIGURES_DIR, "SHAP_Waterfall.png")
YIELD_FUSION_COMPARISON_PATH = os.path.join(YIELD_FIGURES_DIR, "fusion_comparison.png")
