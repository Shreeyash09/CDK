from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2    
    # aws_sqs as sqs,
)
from constructs import Construct

class VpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc",
            ip_addresses=ec2.IpAddresses.cidr("10.10.0.0/16"),
            max_azs=2,
            nat_gateways=1,
            reserved_azs=0,
            vpc_name="Shreeyash-cdk-vpc" 
        )
