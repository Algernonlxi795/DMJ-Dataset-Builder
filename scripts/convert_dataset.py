from configs.settings import (
    RAW_DATASET_DIR,
    PROCESSED_DATASET_DIR,
)

from core.converter import DatasetConverter

converter = DatasetConverter()

converter.convert_file(
    dataset_name="Magicoder-OSS-Instruct-75K",
    input_file=f"{RAW_DATASET_DIR}/ise-uiuc__Magicoder-OSS-Instruct-75K.jsonl",
    output_file=f"{PROCESSED_DATASET_DIR}/magicoder.jsonl"
)