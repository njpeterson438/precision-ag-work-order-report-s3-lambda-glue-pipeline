import json
import boto3
import os

# Create a Glue client
glue = boto3.client('glue')

def lambda_handler(event, context):
    try:
        # Extract bucket and object key from the S3 event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        file_path = f"s3://{bucket_name}/{object_key}"

        # Get Glue job name from environment variable
        glue_job_name = os.environ.get("GLUE_JOB_NAME", "your-glue-job-name")

        # Optional: Only proceed if the file is an .xlsx
        if not object_key.lower().endswith('.xlsx'):
            print(f"Skipping non-Excel file: {object_key}")
            return {
                'statusCode': 200,
                'body': json.dumps("File skipped (not an .xlsx)")
            }

        print(f"Triggering Glue job '{glue_job_name}' with file: {file_path}")

        # Start the Glue job with input file argument
        response = glue.start_job_run(
            JobName=glue_job_name,
            Arguments={
                "--INPUT_FILE": file_path
            }
        )

        print(f"Glue job '{glue_job_name}' started successfully.")
        return {
            'statusCode': 200,
            'body': json.dumps(f"Glue job triggered for {file_path}")
        }

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error triggering Glue job: {str(e)}")
        }
