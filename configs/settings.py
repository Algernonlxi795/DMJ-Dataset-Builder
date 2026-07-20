"""
DMJ Dataset Builder Configuration
"""

# =====================================
# Project
# =====================================

PROJECT_NAME = "DMJ Dataset Builder"

AUTHOR = "Durvesh Jadhav"

LICENSE = "MIT"

# =====================================
# Dataset
# =====================================

DATASET_NAME = "DMJ Dataset"

DATASET_VERSION = "1.0.0"

DATASET_PREFIX = "DMJ-DS"

# =====================================
# Directories
# =====================================

RAW_DATASET_DIR = "datasets/raw"

PROCESSED_DATASET_DIR = "datasets/processed"

FINAL_DATASET_DIR = "datasets/final"

REPORTS_DIR = "reports"

# =====================================
# Output
# =====================================

FINAL_DATASET_NAME = (
    f"dmj_dataset_v{DATASET_VERSION}.jsonl"
)