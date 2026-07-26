"""
Central configuration for AgriVision AI.

Every path the app touches lives here. To add a new model, retrain an existing one,
or reorganize files, this is the ONLY file you should need to edit — nothing else
in src/ or app.py hardcodes a filename.
"""

import os

# ------------------------------------------------------------------
# Folders
# ------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root
MODELS_DIR = os.path.join(BASE_DIR, "models")

# ------------------------------------------------------------------
# Disease detection branch
# ------------------------------------------------------------------
DISEASE_MODEL_PATH = os.path.join(MODELS_DIR, "best_disease_model.keras")
DISEASE_META_PATH = os.path.join(MODELS_DIR, "disease_meta.joblib")
IMG_SIZE_CNN = 224

# ------------------------------------------------------------------
# Encoders (shared by all yield models)
# ------------------------------------------------------------------
FUSION_ENCODERS_PATH = os.path.join(MODELS_DIR, "fusion_encoders.joblib")  # preferred, combined
AREA_ENCODER_PATH = os.path.join(MODELS_DIR, "area_encoder.pkl")           # fallback, separate
ITEM_ENCODER_PATH = os.path.join(MODELS_DIR, "item_encoder.pkl")           # fallback, separate

# ------------------------------------------------------------------
# Yield prediction branch
# ------------------------------------------------------------------
YIELD_MODEL_ENDTOEND_PATH = os.path.join(MODELS_DIR, "fused_yield_model_endtoend.joblib")
YIELD_MODEL_ORACLE_PATH = os.path.join(MODELS_DIR, "fused_yield_model_oracle.joblib")
YIELD_MODEL_BASELINE_PATH = os.path.join(MODELS_DIR, "baseline_yield_model.joblib")

BASE_FEATURES = [
    "Area_enc", "Item_enc", "Year",
    "average_rain_fall_mm_per_year", "pesticides_tonnes", "avg_temp",
]
# Each yield model variant was trained with a DIFFERENT feature set -- the baseline model
# has no severity column at all, and the two fused models used different column names.
# Using the wrong one raises a scikit-learn "feature names should match those passed
# during fit" error, so these three names must stay in sync with how each .joblib was trained.
SEVERITY_FEATURE_ENDTOEND = "disease_severity_endtoend"
SEVERITY_FEATURE_ORACLE = "disease_severity_oracle"

# The disease model only recognizes these 3 crops. The yield dataset's "Item" column
# has dozens of unrelated crops/countries -- without this mapping, the Full Pipeline
# tab would let someone detect "Potato Late Blight" and then forecast yield for
# "Rice", which breaks the actual combination the problem statement calls for.
#
# NOTE: this must be an EXACT match against the yield dataset's Item values, not a
# substring check -- "sweet potatoes" contains the substring "potato" and would
# incorrectly match a loose "in" check.
CROP_EXACT_MATCHES = {
    "potato": {"potato", "potatoes"},
    "corn": {"maize", "corn"},          # PlantVillage labels this class "Corn_(maize)___..."
    "soybean": {"soybean", "soybeans"},
}

# ------------------------------------------------------------------
# Static validation figures from 07_Diseases_Detection_Model.ipynb
# (disease_detection_figures/ in your repo). These are shown in an optional
# "Model validation" section -- not part of the live prediction flow, but
# supporting evidence: confusion matrix + secondary SHAP-on-XGBoost validation,
# per your README's "dual explainability" framing.
# ------------------------------------------------------------------
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SAMPLE_LEAF_PATH = os.path.join(ASSETS_DIR, "sample_images", "sample_leaf.jpg")
HERO_IMAGE_PATH = os.path.join(ASSETS_DIR, "hero.jpg")
DISEASE_FIGURES_DIR = os.path.join(ASSETS_DIR, "disease_detection_figures")
DISEASE_CONFUSION_MATRIX_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_confusion_matrix.png")
DISEASE_GRADCAM_SAMPLE_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_gradcam.png")
DISEASE_OCCLUSION_SALIENCY_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_occlusion_saliency.png")
DISEASE_SHAP_FEATURE_IMPORTANCE_PATH = os.path.join(DISEASE_FIGURES_DIR, "disease_shap_feature_importance.png")

# Yield-side validation figures (from 04_Explainable_AI.ipynb / 08_Model_Integration_.ipynb),
# sitting at your repo root as SHAP_Bar.png / SHAP_Beeswarm.png / SHAP_Waterfall.png /
# fusion_comparison.png. Shown in the same "Model validation" section as the disease figures.
YIELD_FIGURES_DIR = os.path.join(ASSETS_DIR, "yield_figures")
YIELD_SHAP_BAR_PATH = os.path.join(YIELD_FIGURES_DIR, "SHAP_Bar.png")
YIELD_SHAP_BEESWARM_PATH = os.path.join(YIELD_FIGURES_DIR, "SHAP_Beeswarm.png")
YIELD_SHAP_WATERFALL_PATH = os.path.join(YIELD_FIGURES_DIR, "SHAP_Waterfall.png")
YIELD_FUSION_COMPARISON_PATH = os.path.join(YIELD_FIGURES_DIR, "fusion_comparison.png")

# ------------------------------------------------------------------
# To add a NEW model later (e.g. a v2 disease model or an extra yield variant):
#   1. Drop the file in models/
#   2. Add a path constant here
#   3. Add a loader function in src/model_loader.py
#   4. Use it from app.py
# ------------------------------------------------------------------
