import json
from pathlib import Path
from core.metadata import MetadataEnricher
from core.id_generator import IDGenerator

from registry.importer_registry import ImporterRegistry


class DatasetConverter:

    def __init__(self):
        self.registry = ImporterRegistry()
        self.enricher = MetadataEnricher()
        self.id_generator = IDGenerator()

    def convert_file(
        self,
        dataset_name,
        input_file,
        output_file
    ):

        importer = self.registry.get(dataset_name)

        Path(output_file).parent.mkdir(parents=True, exist_ok=True)

        converted = 0

        with open(input_file, encoding="utf-8") as fin, \
             open(output_file, "w", encoding="utf-8") as fout:

            for line in fin:

                record = json.loads(line)

                dmj = importer.convert(record)
                dmj = self.enricher.enrich(dmj)
                dmj["id"] = self.id_generator.next_id()

                fout.write(
                    json.dumps(dmj, ensure_ascii=False)
                )

                fout.write("\n")

                converted += 1

        print(f"Converted {converted} records.")