import boto3

def create_ec2_instance():
    try:
        print("Creating EC2 instances")
        resource_ec2 = boto3.client('ec2')

        # Define MinCount and MaxCount as integers
        MinCount = 1
        MaxCount = 3

        # Create instances
        response = resource_ec2.run_instances(
            ImageId="ami-04b6019d38ea93034",
            InstanceType='t2.micro',
            MinCount=MinCount,
            MaxCount=MaxCount,
            KeyName="test",
            SecurityGroupIds=[
                'sg-0dbfeca0284dcad61'
            ]
        )

        # Print the instance IDs and set unique tags
        for i, instance in enumerate(response['Instances'], start=1):
            instance_id = instance['InstanceId']
            print("Instance ID created is: {} Instance type created is: {}".format(instance_id, instance['InstanceType']))

            # Tag each instance with a unique name
            resource_ec2.create_tags(
                Resources=[instance_id],
                Tags=[{'Key': 'Name', 'Value': f'MyInstance_{i}'}]
            )

    except Exception as e:
        print("An error occurred:", e)

create_ec2_instance()

