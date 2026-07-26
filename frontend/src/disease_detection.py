import numpy as np

from src import config
from src.grad_cam import compute_heatmap, overlay_heatmap


def preprocess_image(pil_img):
    img = pil_img.convert("RGB").resize((config.IMG_SIZE_CNN, config.IMG_SIZE_CNN))
    arr = np.array(img, dtype=np.float32)
    return np.expand_dims(arr, axis=0), img


def severity_level(score):
    if score < 0.15:
        return "green", "Healthy"
    if score < 0.5:
        return "yellow", "Mild"
    return "red", "Severe"


def predict(model, meta, pil_img, with_gradcam=True):
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
        return result, None, "failed"

    if heatmap is None:
        return result, None, "unavailable"

    overlay = overlay_heatmap(resized, heatmap)
    return result, overlay, "ok"