import json
from collections import Counter


class DatasetStats:

    def generate(self, dataset_file):

        total = 0

        languages = Counter()
        topics = Counter()
        difficulties = Counter()

        total_tokens = 0
        code_examples = 0

        with open(dataset_file, encoding="utf-8") as f:

            for line in f:

                total += 1

                record = json.loads(line)

                meta = record["metadata"]

                languages[meta["language"]] += 1
                topics[meta["topic"]] += 1
                difficulties[meta["difficulty"]] += 1

                total_tokens += meta["estimated_tokens"]

                if meta["has_code"]:
                    code_examples += 1

        print("=" * 50)
        print("DMJ DATASET REPORT")
        print("=" * 50)

        print(f"\nTotal Records : {total}")

        print("\nLanguages")
        print("-" * 20)

        for lang, count in languages.most_common():
            print(f"{lang:<15} {count}")

        print("\nTopics")
        print("-" * 20)

        for topic, count in topics.most_common():
            print(f"{topic:<20} {count}")

        print("\nDifficulty")
        print("-" * 20)

        for diff, count in difficulties.most_common():
            print(f"{diff:<15} {count}")

        print(f"\nAverage Tokens : {total_tokens // total}")

        print(f"\nCode Examples : {code_examples}")
        print(f"Text Examples : {total - code_examples}")