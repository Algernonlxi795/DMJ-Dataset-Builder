from importers.magicoder import MagicoderImporter


class ImporterRegistry:

    def __init__(self):
        self.importers = {
            "Magicoder-OSS-Instruct-75K": MagicoderImporter(),
        }

    def get(self, dataset_name):
        if dataset_name not in self.importers:
            raise ValueError(
                f"No importer registered for {dataset_name}"
            )

        return self.importers[dataset_name]