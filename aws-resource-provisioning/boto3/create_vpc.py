import boto3
from config.config import REGION, VPC_CIDR

ec2 = boto3.client("ec2", region_name=REGION)

response = ec2.create_vpc(
    CidrBlock=VPC_CIDR
)

vpc_id = response["Vpc"]["VpcId"]

print("VPC Created")
print(vpc_id)
