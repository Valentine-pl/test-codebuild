#put_s3

import boto3
from datetime import datetime
from aws_config import AWS_ACCESS_KEY_ID, AWS_DEFAULT_REGION, AWS_SECRET_ACCESS_KEY


# Initialize the S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

# Determine the partition values
current_date = datetime.now()
year, month, day, hour, minute = current_date.strftime("%Y"), current_date.strftime("%m"), current_date.strftime("%d"), current_date.strftime("%H"), current_date.strftime("%M")
partition_path = f"year={year}/month={month}/day={day}/hour={hour}/minute={minute}/"

# Specify the bucket name and file details
file_path = 'fake_data.csv'
bucket_name = 'vp-test-coudbuilder'
object_name = f'data/faker_database/faker_csv/{partition_path}faker_data.csv'  # This specifies a directory within the bucket

# Upload the file
s3.upload_file(file_path, bucket_name, object_name)

print(f"File {file_path} uploaded to {bucket_name}/{object_name}")