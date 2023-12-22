#!/usr/bin/env python3
import os

import aws_cdk as cdk

from rds.rds_stack import RdsStack
from rds.subnet_group_stack import SubnetGroupName

app = cdk.App()

env=cdk.Environment(account='221192224682', region='ap-south-1')

# SubnetGroupName(app, "ASubnetStack", env=env)
RdsStack(app, "RdsStack", env=env)

app.synth()
