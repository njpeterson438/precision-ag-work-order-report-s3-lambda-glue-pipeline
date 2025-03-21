#!/usr/bin/env python
# coding: utf-8

"""
Generalized ETL script for processing Excel files via AWS Lambda and Glue.
Originally developed for ag workflows — now abstracted for open use.
"""

import os
import sys
import json
import boto3
import pandas as pd
from datetime import datetime

# Read input file path from environment variable or CLI argument
input_file = os.getenv("INPUT_FILE")
if not input_file and "--INPUT_FILE" in sys.argv:
    input_file = sys.argv[sys.argv.index("--INPUT_FILE") + 1]
if not input_file:
    raise ValueError("ERROR: INPUT_FILE argument is missing.")

print(f"Processing file: {input_file}")

# Generate output filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
processed_filename = f"processed_report_{timestamp}.csv"
output_file = f"/tmp/{processed_filename}"

# S3 client and target bucket
s3 = boto3.client("s3")
output_bucket = os.getenv("OUTPUT_BUCKET", "your-output-bucket-name")
local_file = "/tmp/temp_file.xlsx"

# Function to load Excel file from S3 or local path
def load_excel_file(filepath):
    if filepath.startswith("s3://"):
        bucket_name = filepath.split("/")[2]
        key = "/".join(filepath.split("/")[3:])
        print(f"Downloading file from S3: {filepath}")
        s3.download_file(bucket_name, key, local_file)
        filepath = local_file
    df = pd.read_excel(filepath, engine="openpyxl")
    return df

# Placeholder for loading a product dictionary from S3
def load_product_dictionary():
    """Stub for loading product reference data."""
    print("Downloading product dictionary from S3...")
    # Customize for your own product reference structure
    # Example: Load a CSV into a dictionary for mapping
    return {}

# Placeholder for mapping products
def map_products(df, product_dict):
    """Stub for mapping product names/IDs using a reference dictionary."""
    # Replace this with domain-specific product lookup logic
    return df

# Clean and normalize the dataframe
def clean_data(df, product_dict):
    df.dropna(how="all", inplace=True)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=True).str.replace(r"[^\w\s]", "", regex=True)

    # Example: Rename or split fields if necessary
    # TODO: Add logic to split 'customer' into name and ID if applicable

    # Example: Apply custom mapping (optional)
    if "product" in df.columns:
        df = map_products(df, product_dict)

    # Example: Apply forward fill for continuity within grouped data
    # TODO: Replace with actual domain fields if needed
    fill_columns = ["status", "field", "job_id"]  # Placeholder columns
    existing_cols = [col for col in fill_columns if col in df.columns]
    if existing_cols:
        df[existing_cols] = df.groupby("job_id", group_keys=False)[existing_cols].apply(lambda x: x.ffill())

    return df

# Load, process, and upload
df = load_excel_file(input_file)
product_dict = load_product_dictionary()
df_cleaned = clean_data(df, product_dict)
df_cleaned.to_csv(output_file, index=False)
print(f"Processed file saved locally: {output_file}")

# Upload to S3 (paths are generalized)
processed_s3_key = f"processed_reports/{processed_filename}"
s3.upload_file(output_file, output_bucket, processed_s3_key)
print(f"ETL process complete. File uploaded to s3://{output_bucket}/{processed_s3_key}")
