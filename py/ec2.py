import boto3

# Replace these values with your own
AMI_ID = 'ami-0c94855ba95c71c99'  # Example: Amazon Linux 2 AMI
INSTANCE_TYPE = 't2.micro'         # Instance type
KEY_NAME = 'your-key-pair'         # Your key pair name
SECURITY_GROUP = 'your-security-group-id'  # Your security group ID
SUBNET_ID = 'your-subnet-id'       # Your subnet ID

def launch_ec2_instance():
    # Initialize a session using Amazon EC2
    ec2 = boto3.client('ec2')

    # Launch the instance
    response = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SecurityGroupIds=[SECURITY_GROUP],
        SubnetId=SUBNET_ID,
        MinCount=1,  # Minimum number of instances to launch
        MaxCount=1   # Maximum number of instances to launch
    )

    # Extracting instance ID from the response
    instance_id = response['Instances'][0]['InstanceId']
    print(f'Launched EC2 Instance with ID: {instance_id}')

if __name__ == "__main__":
    launch_ec2_instance()
