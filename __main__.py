import pulumi
import pulumi_aws as aws

size = 't2.micro'
ami = aws.get_ami(most_recent="true",
                  owners=["137112412989"],
                  filters=[{"name":"name","values":["amzn-ami-hvm-*"]}])
#Create Security Group
group = aws.ec2.SecurityGroup('webserver-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 63375, 'to_port': 63375, 'cidr_blocks': ['0.0.0.0/0']}
    ],
    egress=[aws.ec2.SecurityGroupEgressArgs(
                                    from_port=0,
                                    to_port=0,
                                    protocol="-1",
                                    cidr_blocks=["0.0.0.0/0"],)])
user_data = """
#!/bin/bash
pip3 install fastapi
pip3 install uvicorn
pip3 install requests
sudo yum install -y git
git clone https://github.com/JinZhuAW/PokemonGuesserAPI.git
cd PokemonGuesserAPI
"""
#Create ec2 instance
server = aws.ec2.Instance('webserver-www',
    instance_type=size,
    key_name = 'vockey',
    vpc_security_group_ids=[group.id], # reference security group from above
    user_data=user_data,
    ami='ami-0ca285d4c2cda3300')

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)