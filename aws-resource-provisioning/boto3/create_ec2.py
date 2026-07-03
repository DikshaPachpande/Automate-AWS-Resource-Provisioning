import boto3
from config.config import REGION
from config.config import AMI_ID
from config.config import INSTANCE_TYPE
from config.config import KEY_NAME

ec2 = boto3.resource("ec2", region_name=REGION)

instance = ec2.create_instances(
    ImageId=AMI_ID,
    MinCount=1,
    MaxCount=1,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME
)

print("EC2 Instance Created")

print(instance[0].id)
