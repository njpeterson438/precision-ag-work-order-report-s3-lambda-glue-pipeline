# config.py

"""
Configuration file for environment variables and reusable constants
used across the ETL pipeline.
"""

import os

# S3 Buckets
INPUT_BUCKET = os.getenv("INPUT_BUCKET", "your-input-bucket-name")
OUTPUT_BUCKET = os.getenv("OUTPUT_BUCKET", "your-output-bucket-name")

# Product Dictionary (optional lookup file)
PRODUCT_DICT_BUCKET = os.getenv("PRODUCT_DICT_BUCKET", "your-product-bucket-name")
PRODUCT_DICT_KEY = os.getenv("PRODUCT_DICT_KEY", "product_lookup.csv")

# Local temporary paths
TEMP_DOWNLOAD_PATH = "/tmp/temp_file.xlsx"
PRODUCT_DICT_LOCAL_PATH = "/tmp/product_dict.csv"

# Output path for processed files (relative key in S3)
PROCESSED_S3_PREFIX = "processed_reports/"
PROCESSED_FILE_NAME_TEMPLATE = "processed_report_{timestamp}.csv"

# General flags
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
