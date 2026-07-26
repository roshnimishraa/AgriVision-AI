# AgriVision AI Frontend

**AgriVision AI: An Explainable Multimodal System for Crop Disease Detection and Yield Prediction**

AgriVision AI is an explainable, multimodal agricultural intelligence tool built with Streamlit. It combines a CNN-based crop disease classifier with a fused yield-prediction model, so a user can upload a leaf photo, provide field conditions, and get both a disease diagnosis and a yield forecast — each backed by an explainability view (Grad-CAM for the image model, SHAP for the yield model).

## Features

- **Disease Detection** — Upload a leaf image to instantly detect crop disease.
- **Grad-CAM Heatmaps** — Visualize exactly which regions of the leaf influenced the model's decision.
- **Yield Forecasting** — Predict expected crop yield based on real-world field conditions.
- **Disease-Aware Comparison** — Quantify how disease severity impacts projected yield outcomes.
- **SHAP Explanations** — Understand the reasoning behind each prediction with transparent, feature-level insights.
- **One-Click PDF Reports** — Generate a shareable report summarizing the full analysis.
- **Model Validation Dashboard** — Review performance metrics and diagnostics for complete model transparency.
- **Sample Photo** — Explore the tool's full capabilities instantly, without needing to upload an image.

## Tech stack

- Streamlit for the UI
- TensorFlow for the disease classifier
- scikit-learn for the yield models and encoders
- SHAP for explainability
- fpdf2 for PDF report generation
- Hugging Face Hub for model storage

## Project structure

```
frontend/
├── app.py                     # Entry point: applies theme, renders navbar + current page
├── requirements.txt
├── runtime.txt                 # Python version
├── assets/
│   ├── hero.jpg
│   ├── sample_images/           # Sample leaf photo (Soyabeans) used by "Try a sample photo"
│   ├── disease_figures/         # Validation figures for the disease model
│   └── yield_figures/           # Validation figures for the yield model
├── models/                      # Local copies of trained models (NOT used at runtime — see below)
└── src/
    ├── config.py                 # Paths, filenames, feature lists, crop-name matching
    ├── model_downloader.py        # Pulls model files from Hugging Face Hub into hf_models/
    ├── model_loader.py             # Loads/caches models & encoders for use in the app
    ├── disease_detection.py        # Disease inference + severity scoring
    ├── grad_cam.py                  # Grad-CAM heatmap generation
    ├── yield_prediction.py           # Yield model inference
    ├── yield_explainability.py        # SHAP explanations for yield predictions
    ├── report_generator.py             # Builds the downloadable PDF report
    └── ui/
        ├── styles.py             # Global CSS
        ├── components.py          # Navbar, hero sections, step indicator, cards
        ├── about_page.py           # Landing page
        ├── unified_page.py          # Main tool: upload → analyze → results → report
        ├── theme.py                  # Re-exports the public UI
        └── html_utils.py               # Helper for rendering raw HTML blocks
```

### About the `models/` folder

The app does **not** read model files from the local `models/` folder at runtime. Instead, `src/model_downloader.py` downloads each required file from the Hugging Face repo set in `src/config.py` into a local `hf_models/` cache directory the first time it's needed. The `models/` folder (and the `.keras`/`.joblib`/`.pkl` files in it) can be kept locally for reference, but doesn't need to be shipped with the app.

## Setup

```bash
# from the project root
python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Running the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` by default. The first run will download model files from Hugging Face Hub, so it needs an internet connection the first time.
