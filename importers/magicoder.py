from importers.base import BaseImporter


class MagicoderImporter(BaseImporter):

    NAME = "Magicoder"

    def convert(self, record):

        return {
            "instruction": record.get("problem", "").strip(),
            "input": "",
            "output": record.get("solution", "").strip(),

            "metadata": {
                "language": record.get("lang", "unknown"),
                "category": "Programming",
                "difficulty": "Unknown",
                "source": "Magicoder-OSS-Instruct-75K"
            }
        }