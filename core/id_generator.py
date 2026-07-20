from configs.settings import (
    DATASET_PREFIX,
    DATASET_VERSION,
)


class IDGenerator:

    def __init__(self):

        self.counter = 1

    def next_id(self):

        uid = (
            f"{DATASET_PREFIX}-"
            f"{DATASET_VERSION}-"
            f"{self.counter:08d}"
        )

        self.counter += 1

        return uid