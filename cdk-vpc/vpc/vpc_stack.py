from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_cloudformation as cfn    
    # aws_sqs as sqs,
)
from constructs import Construct

class VpcStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc",
            ip_addresses=ec2.IpAddresses.cidr("169.10.0.0/16"),
            max_azs=2,
            nat_gateways=1,
            reserved_azs=0,
            vpc_name="Shreeyash-cdk-vpc",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                # Public subnets
                ec2.SubnetConfiguration(
                    name="snet-public-subnet-01",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=22,
                    map_public_ip_on_launch=True,
                ),
                # Private with internet subnets
                ec2.SubnetConfiguration(
                    name="snet-private-internet-subnet-01",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    cidr_mask=22,
                ),
                # Private subnet
                ec2.SubnetConfiguration(
                    name="snet-private-subnet-01",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=22,
                ),
            ],
            )
        # CreateRoutetable from vpc         
        route_table = ec2.CfnRouteTable(self, "MyCfnRouteTable",
                                vpc_id=vpc.vpc_id
            )
        # CreateRoute from subnets
        cfn_subnet_route_table_association = ec2.CfnSubnetRouteTableAssociation(self, "MyCfnSubnetRouteTableAssociation",
                route_table_id=route_table.attr_route_table_id,
                subnet_id=vpc.private_subnets[0].subnet_id
            )        
        # route = ec2.CfnRoute(self, "Route", 
        #             route_table_id=route_table.attr_route_table_id,
        #             destination_cidr_block="169.10.0.0/22",
        #             nat_gateway_id="nat-07d38e933babbc9b2"
        #   )
        


        
