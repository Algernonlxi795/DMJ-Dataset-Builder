"""
Base Importer

Every dataset importer inherits from this class.
"""


class BaseImporter:
    NAME = "Base Importer"

    def convert(self, record):
        """
        Convert one record into the DMJ format.

        Must return a dictionary.
        """
        raise NotImplementedError("Importer must implement convert()")