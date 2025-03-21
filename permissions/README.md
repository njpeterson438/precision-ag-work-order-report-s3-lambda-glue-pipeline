# permissions/

This folder contains example IAM and S3 policies used to configure the AWS services required for the pipeline.

These JSON files are simplified templates and **must be customized** with your specific bucket names, ARNs, and account IDs before use.

## Files:

### `s3-bucket-policy.json`
Defines a sample S3 bucket policy that grants access to:
- AWS Lambda (to read objects)
- AWS Glue (to read/write objects and list the bucket)

This policy is attached directly to the S3 bucket to allow these services to interact with its contents.

---

### `lambda-trust-policy.json`
IAM trust policy that allows the **Lambda service** (`lambda.amazonaws.com`) to assume the associated IAM role.

Use this when creating a Lambda execution role to bind the service to its permissions.

---

### `lambda-permissions-policy.json`
IAM permissions policy for the Lambda function role, granting it access to:
- Read from the specified S3 bucket
- Start a Glue crawler
- Write logs to CloudWatch

---

### `glue-service-role-policy.json`
IAM policy for the Glue crawler service role. Grants permission to:
- Read/write to the S3 bucket
- Access Glue resources (catalog, jobs, crawlers)

This role is used by the Glue service to crawl the uploaded data and update the Data Catalog.

---

**Note:** Always follow AWS best practices when assigning permissions. Use the principle of least privilege and consider adding resource-specific restrictions when possible.
