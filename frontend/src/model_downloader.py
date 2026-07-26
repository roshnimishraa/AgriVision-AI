import os

from huggingface_hub import hf_hub_download

from src import config


FILES = [
    config.DISEASE_MODEL_FILENAME,
    config.DISEASE_META_FILENAME,
    config.FUSION_ENCODERS_FILENAME,
    config.AREA_ENCODER_FILENAME,
    config.ITEM_ENCODER_FILENAME,
    config.YIELD_MODEL_ENDTOEND_FILENAME,
    config.YIELD_MODEL_ORACLE_FILENAME,
    config.YIELD_MODEL_BASELINE_FILENAME,
]


def download_models():

    os.makedirs(
        config.HF_CACHE_DIR,
        exist_ok=True
    )

    for filename in FILES:

        file_path = os.path.join(
            config.HF_CACHE_DIR,
            filename
        )

        if not os.path.exists(file_path):

            hf_hub_download(
                repo_id=config.HF_MODEL_REPO,
                filename=filename,
                local_dir=config.HF_CACHE_DIR
            )