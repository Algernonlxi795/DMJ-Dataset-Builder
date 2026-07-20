import argparse
import subprocess


parser = argparse.ArgumentParser(
    prog="DMJ Dataset Builder"
)

parser.add_argument(
    "command",
    choices=[
    "download",
    "convert",
    "stats",
    "validate",
    "merge"
]
)

args = parser.parse_args()

COMMANDS = {
    "download": "python -m scripts.download_datasets",
    "convert": "python -m scripts.convert_dataset",
    "stats": "python -m scripts.stats",
    "validate": "python -m scripts.validate",
    "merge": "python -m scripts.merge",
}

subprocess.run(
    COMMANDS[args.command],
    shell=True,
    check=True
)