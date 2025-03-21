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
