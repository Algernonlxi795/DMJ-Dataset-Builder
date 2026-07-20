import json
from collections import Counter


class DatasetValidator:

    REQUIRED_FIELDS = [
        "instruction",
        "input",
        "output",
        "metadata"
    ]

    REQUIRED_METADATA = [
        "language",
        "category",
        "difficulty",
        "topic",
        "estimated_tokens",
        "has_code",
        "source"
    ]

    def validate(self, dataset_file):

        total = 0
        valid = 0

        errors = Counter()

        with open(dataset_file, encoding="utf-8") as f:

            for line in f:

                total += 1

                try:
                    record = json.loads(line)

                except json.JSONDecodeError:
                    errors["Invalid JSON"] += 1
                    continue

                failed = False

                for field in self.REQUIRED_FIELDS:

                    if field not in record:
                        errors[f"Missing {field}"] += 1
                        failed = True

                if failed:
                    continue

                metadata = record["metadata"]

                for field in self.REQUIRED_METADATA:

                    if field not in metadata:
                        errors[f"Missing metadata.{field}"] += 1
                        failed = True

                if failed:
                    continue

                if not record["instruction"].strip():
                    errors["Empty instruction"] += 1
                    continue

                if not record["output"].strip():
                    errors["Empty output"] += 1
                    continue

                if metadata["estimated_tokens"] <= 0:
                    errors["Invalid token count"] += 1
                    continue

                valid += 1

        print("=" * 50)
        print("DMJ DATASET VALIDATION")
        print("=" * 50)

        print(f"\nRecords Checked : {total}")
        print(f"Valid Records   : {valid}")
        print(f"Invalid Records : {total - valid}")

        print("\nErrors")
        print("-" * 30)

        if len(errors) == 0:
            print("No validation errors found.")

        else:
            for error, count in errors.items():
                print(f"{error:<30} {count}")

        print("\nValidation Complete.")