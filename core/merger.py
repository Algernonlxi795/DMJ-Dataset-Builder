import json
import hashlib
from pathlib import Path
from datetime import datetime

from configs.settings import (
    PROCESSED_DATASET_DIR,
    FINAL_DATASET_DIR,
    FINAL_DATASET_NAME,
)


class DatasetMerger:

    def merge(self):

        processed_dir = Path(PROCESSED_DATASET_DIR)

        output_file = Path(FINAL_DATASET_DIR) / FINAL_DATASET_NAME

        output_file.parent.mkdir(parents=True, exist_ok=True)

        seen = set()

        total = 0
        written = 0
        duplicates = 0

        with open(output_file, "w", encoding="utf-8") as fout:

            for dataset in processed_dir.glob("*.jsonl"):

                print(f"Merging {dataset.name}")

                with open(dataset, encoding="utf-8") as fin:

                    for line in fin:

                        total += 1

                        record = json.loads(line)

                        fingerprint = hashlib.sha256(
                            (
                                record["instruction"]
                                + record["output"]
                            ).encode("utf-8")
                        ).hexdigest()

                        if fingerprint in seen:
                            duplicates += 1
                            continue

                        seen.add(fingerprint)

                        fout.write(
                            json.dumps(record, ensure_ascii=False)
                        )

                        fout.write("\n")

                        written += 1

        report = {
            "created_at": datetime.utcnow().isoformat(),
            "datasets_processed": len(
                list(processed_dir.glob("*.jsonl"))
            ),
            "records_before_merge": total,
            "duplicates_removed": duplicates,
            "records_after_merge": written,
            "output_file": str(output_file)
        }

        Path("reports/merge").mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            "reports/merge/merge_report.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                report,
                f,
                indent=4
            )

        print("\nMerge Complete!")
        print(f"Output : {output_file}")
        print(f"Records : {written}")
        print(f"Duplicates Removed : {duplicates}")