# AgriVision AI

## An Explainable System for Crop Disease Detection and Crop Yield Prediction

AgriVision AI is a Machine Learning and Deep Learning based agricultural decision support system with two components: **Crop Disease Detection** from leaf images, and **Crop Yield Prediction** from agricultural and environmental factors. Both are made interpretable through **Explainable AI** techniques — **Grad-CAM** for the image model and **SHAP** for the yield model.

> **The two components are independent.** They are presented together in one interface, but the yield forecast does not use the disease result and the disease classifier does not use field conditions. See [Why there is no fusion](#why-there-is-no-fusion) — this is a property of the datasets, not an oversight.

---


## Features

### Crop Disease Detection
- Classifies crop diseases from leaf images.
- Two-branch feature extraction — classical (HSV, LBP, pixel-ratio features) and CNN (raw images).
- Compares four models: XGBoost, Random Forest, MobileNetV2, EfficientNetB0.
- 8 classes across 3 crops:
  - **Corn (maize)** — Cercospora/Gray leaf spot, Common rust, Northern leaf blight, healthy
  - **Potato** — Early blight, Late blight, healthy
  - **Soybean** — healthy only
- Saved best-performing model for inference.

> Note that **Soybean has no disease class** in this dataset subset — only `Soybean___healthy`. The system can never report a soybean disease.

### Crop Yield Prediction
- Predicts crop yield from region, crop type, year, rainfall, pesticide use and average temperature.
- Compares Linear Regression, Decision Tree and Random Forest.
- Saved trained model and label encoders.

### Web Application
A Streamlit app in [`frontend/`](frontend/) serves both models with Grad-CAM, SHAP and a PDF report. See [frontend/Readme.md](frontend/Readme.md).

---

## Why there is no fusion

The original design called for a "multimodal" system in which disease severity fed the yield model. That is not achievable with these two datasets:

| | PlantVillage | Crop Yield Dataset (FAO) |
|---|---|---|
| One row is | one leaf, lab-photographed | one **country × crop × year** |
| Location | not recorded | national |
| Date | not recorded | year |
| Yield | not recorded | hg/ha, national average |

There is no shared key, and none could exist — a single leaf carries no information about a nation's annual harvest. Notebook 08 originally attached severity values to yield rows using `np.random.choice`, which made the feature statistically independent of the target by construction.

Notebook 08 now keeps that as a labelled **ablation**, and the measured result is unambiguous:

| Model | MAE | R² |
|---|---:|---:|
| Baseline (no severity) — **deployed** | 11331.37 | 0.9447 |
| Synthetic severity, *predicted* | 11291.90 | 0.9463 |
| Synthetic severity, *true* | 11257.94 | 0.9465 |

The severity feature shifts R² by **+0.0017 (0.18%)** — noise, not signal. A random forest given a pure-noise feature can score marginally better, because occasional splits on it decorrelate the trees.

The decisive number is the last row against the middle one: swapping the classifier's *predicted* severity for the *ground-truth* severity changes R² by **0.0001**. If severity carried real information about yield, perfect labels would beat imperfect ones by a visible margin. They don't, because both columns are noise.

That gap was this project's original headline finding, reported as *"the disease model's errors have a negligible effect on yield prediction."* It is a tautology — two independent noise features must perform alike — and says nothing about the classifier.

Two routes to a genuine integration:

1. **Decision-level integration** — keep the models independent and combine them with published yield-loss coefficients per disease (e.g. the [Crop Protection Network disease loss database](https://loss.cropprotectionnetwork.org/about), which covers corn and soybean). The link is explicit and citable rather than learned.
2. **Change the data** — learned fusion requires imagery and yield observed on the same units. County-level satellite datasets such as [CropNet](https://huggingface.co/datasets/CropNet/CropNet) support this; PlantVillage cannot.

---

## A note on "severity"

The severity value attached to each prediction (`healthy` 0.0, `early_blight` 0.3, `late_blight` 0.6, …) is a **hand-authored constant per class**, defined in notebook 07. It is not measured from the image and adds no information beyond the predicted class label. It is displayed as an indicative band only. Replacing it with sourced figures from the extension literature is the intended next step.

---

## Datasets

**Crop Disease Detection** — PlantVillage
https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

**Crop Yield Prediction** — Crop Yield Prediction Dataset
https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset

Neither dataset is included in the repository.

---

## Technologies Used

| Category | Tools |
|---|---|
| Programming Language | Python |
| Data Analysis | NumPy, Pandas |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Deep Learning | TensorFlow |
| Computer Vision | OpenCV, scikit-image |
| Explainable AI | SHAP, Grad-CAM |
| Web App | Streamlit |
| Development Environment | Google Colab, VS Code |

---

## Model Comparison

### Crop Yield Prediction  *verified — temporal split*

Trained on 1990–2009 (23,233 rows), tested on 2010–2013 (5,009 rows).

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| Linear Regression *(one-hot)* | 35934.74 | 54681.68 | 0.6723 |
| Decision Tree | 13975.02 | 34572.59 | 0.8690 |
| **Random Forest** | **11331.37** | **22473.22** | **0.9446** |

The Random Forest row describes the **deployed** model. Notebooks 03 and 08 train it with identical data, features, split, `random_state` and `n_estimators`, so they produce the same model — notebook 08's copy (`baseline_yield_model.joblib`) is the one uploaded to Hugging Face and served by the app.

**What the two methodology fixes actually changed:**

| | Before | After | Cause |
|---|---:|---:|---|
| Linear Regression R² | 0.084 | **0.672** | Label-encoded nominal categories → one-hot. The near-zero score was an encoding artifact, not a property of linear models. |
| Random Forest R² | 0.986 | **0.945** | Random split → temporal split. |
| Random Forest MAE | 3,742 | **11,331** | Same. Honest error is **3× higher**. |

That MAE gap is the leakage, quantified. A random split on a country × crop × year panel scatters near-identical neighbouring years across train and test, so the model was largely recalling yields it had already seen.

### Crop Disease Detection  *verified — held-out test split*

4,660 train / 995 val / 995 test images, capped at 1000 per class, all models trained with balanced class weights. Metrics are from the **test** split, which was not used for hyperparameter selection or epoch monitoring.

| Model | Accuracy | Macro-F1 |
|--------|:--------:|:--------:|
| **EfficientNetB0** | **0.972** | **0.962** |
| XGBoost | 0.970 | 0.955 |
| MobileNetV2 | 0.961 | 0.944 |
| Random Forest | 0.955 | 0.931 |

**Best model: EfficientNetB0** — same winner as before, now on an honest test split.

Scores are *higher* than the previous validation-set numbers despite the stricter evaluation, because the per-class cap went from 300 to 1000 (2,252 → 6,650 images).

`Potato___healthy` remains the weakest class (F1 0.89 for the winning classical model) and the hardest to measure: PlantVillage contains only 152 such images in total, so it has just **22 test samples** regardless of the cap. A single misclassification moves its F1 by ~4.5 points. Macro-F1 weights it equally with classes that have 150.

---

## Installation

```bash
git clone https://github.com/roshnimishraa/AgriVision-AI.git
cd AgriVision-AI
```

Two separate environments — the app pins exact versions to stay compatible with the pickled models, the notebooks don't need to.

For the notebooks (01–04):
```bash
conda env create -f environment.yml
conda activate agrivision
```

For the web app:
```bash
conda env create -f frontend/environment.yml
conda activate agrivision-app
```

**Python 3.11 is required.** TensorFlow 2.20 publishes no wheels for Python 3.14, and on macOS the `tensorflow-cpu` package has no wheels at any version — `frontend/requirements.txt` selects plain `tensorflow` there automatically.

Plain pip works too if you prefer, as long as the interpreter is 3.11:
```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt              # notebooks
pip install -r frontend/requirements.txt     # app
```

---

## Usage

### Notebooks

Download both datasets from the links above. The yield notebooks expect `data/CropYield/yield_df.csv` relative to the repository root; override with the `AGRIVISION_DATA` environment variable if your copy lives elsewhere.

| Notebook | Runs on | Purpose |
|---|---|---|
| 01–04 | Local (Jupyter/VS Code) | Yield pipeline: collection → EDA → model → SHAP |
| 05–07 | **Google Colab** | Disease pipeline: EDA → preprocessing → model + Grad-CAM |
| 08 | **Google Colab** | Baseline yield model + synthetic-severity ablation |

Notebooks 05–08 use Colab-specific calls (`google.colab.files`, `drive.mount`, `!kaggle`) and a GPU. Notebook 08 requires two files produced by notebook 07 (`disease_test_predictions.csv`, `disease_meta.joblib`) to be uploaded manually.

### Web app

```bash
cd frontend
streamlit run app.py
```

Model files download from Hugging Face on first use, so the first run needs an internet connection.

---
