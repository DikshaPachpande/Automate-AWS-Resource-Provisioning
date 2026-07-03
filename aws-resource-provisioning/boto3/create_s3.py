import boto3
from config.config import REGION, S3_BUCKET

s3 = boto3.client("s3", region_name=REGION)

response = s3.create_bucket(
    Bucket=S3_BUCKET,
    CreateBucketConfiguration={
        "LocationConstraint": REGION
    }
)

print("Bucket Created Successfully")
print(response)
