from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_ec2 as ec2,
    aws_rds as rds,
    Fn,
)
from constructs import Construct

class SubnetGroupName(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        subnet_id = ["subnet-0f2f8f9d62b797c1d", "subnet-05aa408bf95698b3b", "subnet-08a940352f6ee9e65"]

        cfn_dBSubnet_group = rds.CfnDBSubnetGroup(self, "MyCfnDBSubnetGroup",
        db_subnet_group_description="dbSubnetGroupDescription",
        subnet_ids=subnet_id,
        db_subnet_group_name = "dbSubnetGroupnameStack"    
    )

