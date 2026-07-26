import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

_grad_submodel_cache = {}


def _get_grad_submodel(model):
    key = id(model)

    if key in _grad_submodel_cache:
        return _grad_submodel_cache[key]

    import tensorflow as tf

    last_conv_layer_name = None

    for layer in reversed(model.layers):
        try:
            shape = layer.output.shape
        except (AttributeError, ValueError):
            continue

        if shape is not None and len(shape) == 4:
            last_conv_layer_name = layer.name
            break

    if last_conv_layer_name is None:
        _grad_submodel_cache[key] = None
        return None

    grad_model = tf.keras.models.Model(
        [model.inputs],
        [model.get_layer(last_conv_layer_name).output, model.output]
    )

    _grad_submodel_cache[key] = grad_model
    return grad_model


def compute_heatmap(model, img_array):
    import tensorflow as tf

    grad_model = _get_grad_submodel(model)

    if grad_model is None:
        return None

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)
        pred_index = tf.argmax(predictions[0])
        class_channel = predictions[:, pred_index]

    grads = tape.gradient(
        class_channel,
        conv_outputs
    )

    pooled_grads = tf.reduce_mean(
        grads,
        axis=(0, 1, 2)
    )

    conv_outputs = conv_outputs[0]

    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0)

    heatmap = heatmap / (
        tf.math.reduce_max(heatmap) + 1e-8
    )

    return heatmap.numpy()


def overlay_heatmap(pil_img, heatmap, alpha=0.4):
    heatmap_img = Image.fromarray(
        np.uint8(255 * heatmap)
    ).resize(pil_img.size)

    cmap = plt.get_cmap("jet")

    heatmap_colored = cmap(
        np.array(heatmap_img) / 255.0
    )[:, :, :3]

    heatmap_colored = Image.fromarray(
        np.uint8(heatmap_colored * 255)
    )

    return Image.blend(
        pil_img.convert("RGB"),
        heatmap_colored,
        alpha
    )
