from core.validator import DatasetValidator

validator = DatasetValidator()

validator.validate(
    "datasets/processed/magicoder.jsonl"
)