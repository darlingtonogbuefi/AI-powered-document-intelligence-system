#  /scripts\upload_s3.py

import os
import sys
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

def upload_files_to_s3(folder_path, bucket_name, prefix=""):
    s3_client = boto3.client('s3')

    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, folder_path)
            s3_key = os.path.join(prefix, relative_path).replace("\\", "/")

            try:
                s3_client.upload_file(local_path, bucket_name, s3_key)
                print(f"Successfully uploaded {relative_path} to {bucket_name}/{s3_key}")
            except ClientError as e:
                print(f"Error uploading {relative_path}: {e}")

if __name__ == "__main__":
    # Load bucket name from environment variable
    bucket_name = os.getenv("S3_BUCKET_NAME")
    if not bucket_name:
        print("Error: S3_BUCKET_NAME is not set in the environment.")
        sys.exit(1)

    # Allow folder path and prefix to be optionally passed as command line arguments
    folder_path = sys.argv[1] if len(sys.argv) > 1 else "scripts/spec-sheets"
    prefix = sys.argv[2] if len(sys.argv) > 2 else "spec-sheets"

    upload_files_to_s3(folder_path, bucket_name, prefix)
