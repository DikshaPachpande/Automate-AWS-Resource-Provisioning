import boto3
from config.config import REGION
from config.config import S3_BUCKET

ec2 = boto3.resource("ec2", region_name=REGION)

# Stop all instances

for instance in ec2.instances.all():
    print("Terminating:", instance.id)
    instance.terminate()

s3 = boto3.resource("s3")

bucket = s3.Bucket(S3_BUCKET)

bucket.objects.all().delete()

bucket.delete()

print("Resources Deleted")
