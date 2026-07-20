from pathlib import Path
import json

from datasets import load_dataset

from configs.settings import DATASETS, RAW_DATASET_DIR


def save_dataset(dataset_name, dataset):
    folder = Path(RAW_DATASET_DIR)
    folder.mkdir(parents=True, exist_ok=True)

    safe_name = dataset_name.replace("/", "__")
    output_file = folder / f"{safe_name}.jsonl"

    print(f"Saving {output_file}")

    with open(output_file, "w", encoding="utf-8") as f:
        for row in dataset:
            f.write(json.dumps(row, ensure_ascii=False))
            f.write("\n")


def download_dataset(dataset_info):

    dataset_id = dataset_info["id"]

    print("=" * 60)
    print(f"Downloading {dataset_id}")

    dataset = load_dataset(dataset_id)

    split = list(dataset.keys())[0]

    save_dataset(dataset_id, dataset[split])

    print("Done")


def main():

    for dataset in DATASETS:

        if dataset["enabled"]:
            download_dataset(dataset)


if __name__ == "__main__":
    main()