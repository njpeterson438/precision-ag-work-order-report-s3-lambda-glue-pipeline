# precision-ag-work-order-report-s3-lambda-glue-pipeline
An AWS pipeline to process precision agriculture work order reports for BI dashboards using automated serverless functions.

This repository contains a simple, modular AWS pipeline that ingests `.xlsx` work order reports uploaded to S3, triggers a Lambda function, and launches an AWS Glue Crawler to update the data catalog for querying in Athena.

Originally developed for agricultural operations, this pipeline is adaptable to any domain that processes tabular field reports into queryable datasets.

## Stack:
- AWS S3 (trigger on upload)
- AWS Lambda (Python)
- AWS Glue Crawler (schema discovery)
- AWS Athena (auto-refreshes table for BI queries)

This project demonstrates a practical AWS serverless architecture using S3, Lambda, Glue, and Athena.  
It is not affiliated with Amazon Web Services or any other company.

See the permissions/ folder for example IAM and S3 policies used to enable this pipeline. All resource ARNs should be customized for your AWS environment.

## Lambda Function: S3 Trigger → Glue Job

The `lambda_function.py` script is the serverless function triggered automatically when a new `.xlsx` file is uploaded to the designated S3 bucket.

### Purpose:
This function extracts the uploaded file's S3 path and initiates a predefined AWS Glue job, passing the S3 file path as a runtime argument. It enables automated ingestion and processing of agricultural work order reports—or any tabular data—into a structured data catalog for querying via Athena or downstream BI tools.

### Features:
- Parses the bucket name and object key from the S3 event
- Filters to only process `.xlsx` files (ignores others)
- Dynamically starts a Glue job using the `boto3` client
- Uses an environment variable `GLUE_JOB_NAME` for flexibility
- Includes logging and basic error handling

### Usage Notes:
- Make sure the Lambda execution role has permissions to:
  - Read from the target S3 bucket
  - Start the specified Glue job
  - Write logs to CloudWatch
- Set the `GLUE_JOB_NAME` environment variable in the Lambda console
- Customize the argument key (`--INPUT_FILE`) if your Glue job uses a different name

See [`lambda_function.py`](lambda_function.py) for the full implementation.
