import boto3

# Replace these values with your own
AMI_ID = 'ami-xxxxxxxxxxxxxxxxx'  # Example: RHEL AMI with GUI support
INSTANCE_TYPE = 't2.large'         # Instance type suitable for GUI
KEY_NAME = 'your-key-pair'         # Your key pair name
SECURITY_GROUP = 'your-security-group-id'  # Your security group ID
SUBNET_ID = 'your-subnet-id'       # Your subnet ID

def launch_rhel_gui_instance():
    ec2 = boto3.client('ec2')

    # Launch the instance
    response = ec2.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SecurityGroupIds=[SECURITY_GROUP],
        SubnetId=SUBNET_ID,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'RHEL-GUI-Instance'
                    }
                ]
            }
        ]
    )

    # Extracting instance ID from the response
    instance_id = response['Instances'][0]['InstanceId']
    print(f'Launched RHEL GUI Instance with ID: {instance_id}')

if __name__ == "__main__":
    launch_rhel_gui_instance()
