#!/usr/bin/env python3
import os

import aws_cdk as cdk

from vpc.vpc_stack import VpcStack


app = cdk.App()

env=cdk.Environment(account='221192224682', region='ap-south-1')

VpcStack(app, "VpcStack",env=env)

app.synth()
