from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_rds as rds,
    Fn,
)
from constructs import Construct

class RdsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        azs = Fn.get_azs()        


        subnet_group = rds.SubnetGroup.from_subnet_group_name(self, "ExistingSubnetGroup",
            subnet_group_name="dbSubnetGroupnameStack"
        )

        vpc = ec2.Vpc.from_vpc_attributes(self, "VPC", availability_zones=azs, vpc_id= "vpc-0bbb4fe2180a2a955")
        instance1 = rds.DatabaseInstance(self, "PostgresInstance1",
            engine=rds.DatabaseInstanceEngine.POSTGRES,
            allocated_storage=20,
            instance_type= ec2.InstanceType("t3.micro"),
            # ec2.InstanceType.of(ec2.InstanceClass.STANDARD3, ec2.InstanceSize.MICRO),
            # vpc_subnets=
            database_name="dev1testing",
            instance_identifier="devtest",
            auto_minor_version_upgrade=False,
            # iops=3000,
            max_allocated_storage=100,
            port=3306,
            # storage_throughput=125,
            subnet_group=subnet_group,
            # Generate the secret with admin username `postgres` and random password
            # credentials=rds.Credentials.from_generated_secret("postgres"),
            vpc=vpc
        )

        