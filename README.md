# AgriVision AI

## An Explainable Multimodal System for Crop Disease Detection and Crop Yield Prediction

AgriVision AI is a Machine Learning and Deep Learning based agricultural decision support system that combines **Crop Disease Detection** and **Crop Yield Prediction** into a single platform. The system detects plant diseases from leaf images, predicts crop yield using agricultural and environmental factors, and improves model transparency through **Explainable AI** techniques such as **SHAP** and **Grad-CAM**.

---

## Features

### Highlights
- Multimodal agricultural intelligence system.
- Combines crop disease detection and crop yield prediction into one pipeline.
- Built using Machine Learning and Deep Learning techniques.
- Explainable AI (SHAP + Grad-CAM) for transparent, trustworthy predictions.
- Modular workflow for easy training, evaluation, and deployment.
- Saved models and preprocessing pipelines for future inference.

---

### Crop Disease Detection
- Classifies crop diseases from leaf images.
- Two-branch feature extraction — classical (HSV, LBP, pixel-ratio features) and CNN (raw images).
- Compares multiple Machine Learning and Deep Learning models:
  - XGBoost
  - Random Forest
  - MobileNetV2
  - EfficientNetB0
- Detects disease across 8 classes spanning 3 crops:
  - Corn (maize)
  - Potato
  - Soybean
- Saved best-performing model (EfficientNetB0) for inference.

---

### Crop Yield Prediction
- Predicts crop yield using agricultural and environmental factors.
- Data preprocessing and feature engineering, including categorical encoding.
- Compares multiple Machine Learning models:
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
- Saved trained model (Random Forest) and label encoders.

---

## Datasets

### Crop Disease Detection
**Dataset:** PlantVillage
**Source:** https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

### Crop Yield Prediction
**Dataset:** Crop Yield Prediction Dataset
**Source:** https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset

---

## Technologies Used

| Category | Tools |
|---|---|
| Programming Language | Python |
| Data Analysis | NumPy, Pandas |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow |
| Computer Vision | OpenCV |
| Explainable AI | SHAP, Grad-CAM |
| Development Environment | Google Colab, VS Code |

---

## Models Implemented

### Crop Disease Detection
| Model |
|--------|
| XGBoost |
| Random Forest |
| MobileNetV2 |
| EfficientNetB0 |

### Crop Yield Prediction
| Model |
|--------|
| Linear Regression |
| Decision Tree Regressor |
| Random Forest Regressor |

---

## Model Comparison

### Crop Yield Prediction

| Model | MAE | RMSE | R² Score |
|------|------:|------:|------:|
| Linear Regression | 62444.31 | 81501.76 | 0.0843 |
| Decision Tree | 4103.84 | 13498.73 | 0.9749 |
| **Random Forest** | **3741.53** | **10190.30** | **0.9857** |

**Best Model:** Random Forest Regressor

### Crop Disease Detection

| Model | Accuracy | Macro-F1 |
|--------|:--------:|:--------:|
| **EfficientNetB0** | **0.956** | **0.954** |
| XGBoost | 0.942 | 0.941 |
| MobileNetV2 | 0.936 | 0.934 |
| Random Forest | 0.931 | 0.930 |

**Best Model:** EfficientNetB0

---

## Explainable AI

### Crop Yield Prediction

The **Random Forest Regressor** is interpreted using **SHAP (SHapley Additive exPlanations)** to improve the transparency of crop yield predictions.

#### SHAP Feature Importance Bar Plot
Ranks the input features based on their overall contribution to crop yield prediction.

<img width="2936" height="1243" alt="SHAP Feature Importance" src="https://github.com/user-attachments/assets/613f806b-b6dd-47db-b041-0286971afce6" />

#### SHAP Beeswarm Plot
Shows how each feature positively or negatively influences crop yield predictions across all samples.

<img width="2778" height="1121" alt="SHAP Beeswarm Plot" src="https://github.com/user-attachments/assets/9264504d-6866-40df-88af-5b62b02bb8ce" />

#### SHAP Waterfall Plot
Explains an individual crop yield prediction by showing the contribution of each feature.

<img width="3263" height="1313" alt="SHAP Waterfall Plot" src="https://github.com/user-attachments/assets/002901fc-3815-4eb2-ad67-983edfc9cd44" />

---

### Crop Disease Detection

The selected **EfficientNetB0** model is interpreted using **Grad-CAM**, while **SHAP** is applied to the classical XGBoost model for additional validation.

#### Grad-CAM Heatmap
Grad-CAM highlights the regions of a leaf image that most influenced the CNN's disease classification, making the model's predictions more interpretable.

<img width="834" height="124" alt="Grad-CAM Heatmap" src="https://github.com/user-attachments/assets/c8c2ce98-bd0f-4433-b6b8-e10fcf71eaf1" />

#### SHAP Explanation (XGBoost)
SHAP was applied to the classical XGBoost model to identify the engineered image features that contributed most to disease classification. The results provide an additional explanation and help validate the decisions made by the deep learning model.

<img width="955" height="535" alt="SHAP Explanation" src="https://github.com/user-attachments/assets/a466efc8-98c7-4b0e-aced-43fba4b5afb6" />

---

## Installation

Clone the repository:
```bash
git clone https://github.com/roshnimishraa/AgriVision-AI.git
```

Move to the project directory:
```bash
cd AgriVision-AI
```

Install dependencies:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib shap jupyter ipykernel xgboost opencv-python tensorflow
```

---

## Usage

Run notebooks `01` → `04` for the yield pipeline, then `05` → `07` for the disease detection pipeline. Datasets aren't included — download them from the links in the [Datasets](#datasets) section.

---
