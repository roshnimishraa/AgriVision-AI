# AgriVision AI

## An Explainable Multimodal System for Crop Disease Detection and Crop Yield Prediction

AgriVision AI is a Machine Learning and Deep Learning based agricultural decision support system that combines **Crop Disease Detection** and **Crop Yield Prediction** into a single platform. The system detects plant diseases from leaf images, predicts crop yield using agricultural and environmental factors, and improves model transparency through **Explainable AI** techniques such as **SHAP** and **Grad-CAM**.

---

## Features

### General Features

- Multimodal agricultural intelligence system.
- Combines crop disease detection and crop yield prediction.
- Built using Machine Learning and Deep Learning techniques.
- Explainable AI for transparent predictions.
- Modular workflow for easy training, evaluation, and deployment.
- Saved models and preprocessing pipelines for future inference.

---

### Crop Disease Detection

- Automatic crop disease classification from leaf images.
- Image preprocessing using resizing and normalization.
- Disease prediction across **38 plant disease and healthy classes**.
- Comparative analysis of multiple Deep Learning and Machine Learning models:
  - Custom CNN
  - MobileNetV2
  - EfficientNetB0
  - XGBoost + Random Forest Baseline
- Performance comparison for selecting the most suitable model.
- Model saved for deployment and inference.
- Explainability using Grad-CAM.

---

### Crop Yield Prediction

- Crop yield prediction using agricultural and environmental factors.
- Data preprocessing and feature engineering.
- Comparison of multiple Machine Learning models:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
- Predicts crop yield using:
  - Area
  - Crop Type
  - Year
  - Rainfall
  - Pesticides
  - Average Temperature
- Saved trained model and label encoders.

---

### Explainable AI

#### Crop Yield Prediction

- SHAP Feature Importance
- SHAP Beeswarm Plot
- SHAP Waterfall Plot

#### Crop Disease Detection

- Grad-CAM Heatmap Visualization
- Visual explanation of disease predictions
- Region-based interpretation of infected leaf images

---

# Datasets

## Crop Disease Detection

**Dataset:** PlantVillage

**Source:** https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

## Crop Yield Prediction

**Dataset:** Crop Yield Prediction Dataset

**Source:** https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset

---

# Technologies Used

### Programming Language

- Python

### Data Analysis

- NumPy
- Pandas

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

### Deep Learning

- TensorFlow

### Computer Vision

- OpenCV

### Explainable AI

- SHAP
- Grad-CAM

### Development Environment

- Jupyter Notebook
- Google Colab
- VS Code

---

# Models Implemented

## Crop Disease Detection

| Model | Purpose |
|--------|---------|
| Custom CNN | Deep Learning Baseline |
| MobileNetV2 | Transfer Learning |
| EfficientNetB0 | Transfer Learning |
| XGBoost + Random Forest | Machine Learning Baseline |

---

## Crop Yield Prediction

| Model |
|--------|
| Linear Regression |
| Decision Tree Regressor |
| Random Forest Regressor |

---

# Model Comparison

## Crop Yield Prediction

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| Linear Regression | 62444.31 | 81501.76 | 0.0843 |
| Decision Tree | 4103.84 | 13498.73 | 0.9749 |
| **Random Forest** | **3741.53** | **10190.30** | **0.9857** |

**Best Model:** Random Forest Regressor

---

## Crop Disease Detection

Four different models were trained and compared:

- Custom CNN
- MobileNetV2
- EfficientNetB0
- XGBoost + Random Forest Baseline

<!-- The final model was selected based on comparative evaluation using classification metrics such as Accuracy, Precision, Recall, and F1-Score. -->

<!-- > **Note:** Add the comparison table here after obtaining the final evaluation results. -->

---

# Explainable AI

## Crop Yield Prediction

The Random Forest model is interpreted using **SHAP (SHapley Additive exPlanations)**.

Implemented visualizations include:

### SHAP Feature Importance Bar Plot

Ranks agricultural features based on their overall contribution to crop yield prediction.

<img width="2936" height="1243" alt="image" src="https://github.com/user-attachments/assets/613f806b-b6dd-47db-b041-0286971afce6" />

---

### SHAP Beeswarm Plot

Shows how each feature positively or negatively influences predictions across all samples.

<img width="2778" height="1121" alt="image" src="https://github.com/user-attachments/assets/9264504d-6866-40df-88af-5b62b02bb8ce" />

---

### SHAP Waterfall Plot

Explains individual crop yield predictions by showing feature-wise contributions.

<img width="3263" height="1313" alt="image" src="https://github.com/user-attachments/assets/002901fc-3815-4eb2-ad67-983edfc9cd44" />

---
<!-- 
## Crop Disease Detection

The disease classification model is interpreted using **Grad-CAM**.

Implemented visualization:

- Heatmap highlighting infected regions.
- Visual explanation of CNN predictions.
- Improved transparency of disease detection.

*(Insert Grad-CAM Heatmap)*

---

-->

# Installation

Clone the repository

```bash
git clone https://github.com/roshnimishraa/AgriVision-AI.git
```

Move to the project directory

```bash
cd AgriVision-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---
