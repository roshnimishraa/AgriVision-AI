"""
Disease detection: preprocessing + prediction for the EfficientNetB0 model.
"""

import numpy as np

from src import config
from src.grad_cam import compute_heatmap, overlay_heatmap


def preprocess_image(pil_img):
    """Resizes + batches an uploaded PIL image for the CNN. Returns (array, resized_pil_img)."""
    img = pil_img.convert("RGB").resize((config.IMG_SIZE_CNN, config.IMG_SIZE_CNN))
    arr = np.array(img, dtype=np.float32)
    return np.expand_dims(arr, axis=0), img


def severity_level(score):
    """Returns ('green'|'yellow'|'red', label) for a severity score 0-1, used to
    color-code the result card."""
    if score < 0.15:
        return "green", "Healthy"
    if score < 0.5:
        return "yellow", "Mild"
    return "red", "Severe"


def predict(model, meta, pil_img, with_gradcam=True):
    """Runs disease prediction on a single image.

    Returns (result_dict, overlay_image_or_None, heatmap_status) where result_dict has:
        class, confidence, severity, probs (dict of class -> probability)
    heatmap_status is one of:
        "off"         -- caller chose not to compute it
        "ok"          -- overlay was generated successfully
        "unavailable" -- this model has no identifiable conv layer to explain
        "failed"      -- an unexpected error occurred while computing it
    """
    arr, resized = preprocess_image(pil_img)
    preds = model.predict(arr, verbose=0)[0]

    classes = meta["classes"]
    severity_vec = meta["severity_vec"]
    top_idx = int(np.argmax(preds))

    result = {
        "class": classes[top_idx],
        "confidence": float(preds[top_idx]),
        "severity": float(severity_vec[top_idx]),
        "probs": {classes[i]: float(preds[i]) for i in range(len(classes))},
    }

    if not with_gradcam:
        return result, None, "off"

    try:
        heatmap = compute_heatmap(model, arr)
    except Exception:
        # Grad-CAM is a bonus visualization -- if it fails for any model-specific
        # reason, the disease prediction itself should still be returned.
        return result, None, "failed"

    if heatmap is None:
        return result, None, "unavailable"

    overlay = overlay_heatmap(resized, heatmap)
    return result, overlay, "ok"
