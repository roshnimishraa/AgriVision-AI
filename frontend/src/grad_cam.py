"""
Grad-CAM explainability for the disease-detection CNN.

SPEED FIX: previously the small "gradient sub-model" (conv layer output + final output)
was rebuilt from scratch on every single prediction, which is the main reason
predictions felt slow. It only needs to be built once per loaded model, so it's now
cached at module level keyed by the model's identity.
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

_grad_submodel_cache = {}


def _get_grad_submodel(model):
    """Builds (once per model) a small model exposing [last_conv_output, final_output].
    Cached so repeated predictions on the same loaded model don't rebuild this graph."""
    key = id(model)
    if key in _grad_submodel_cache:
        return _grad_submodel_cache[key]

    import tensorflow as tf

    last_conv_layer_name = None
    for layer in reversed(model.layers):
        try:
            shape = layer.output.shape  # Keras 3 removed layer.output_shape
        except (AttributeError, ValueError):
            continue
        if shape is not None and len(shape) == 4:
            last_conv_layer_name = layer.name
            break

    if last_conv_layer_name is None:
        _grad_submodel_cache[key] = None
        return None

    grad_model = tf.keras.models.Model(
        [model.inputs], [model.get_layer(last_conv_layer_name).output, model.output]
    )
    _grad_submodel_cache[key] = grad_model
    return grad_model


def compute_heatmap(model, img_array):
    """Returns a 2D numpy heatmap (values 0-1) for the model's top predicted class,
    or None if no conv layer could be found."""
    import tensorflow as tf

    grad_model = _get_grad_submodel(model)
    if grad_model is None:
        return None

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-8)
    return heatmap.numpy()


def overlay_heatmap(pil_img, heatmap, alpha=0.4):
    """Blends a heatmap onto the original PIL image for display."""
    heatmap_img = Image.fromarray(np.uint8(255 * heatmap)).resize(pil_img.size)
    cmap = plt.get_cmap("jet")
    heatmap_colored = cmap(np.array(heatmap_img) / 255.0)[:, :, :3]
    heatmap_colored = Image.fromarray(np.uint8(heatmap_colored * 255))
    return Image.blend(pil_img.convert("RGB"), heatmap_colored, alpha)
