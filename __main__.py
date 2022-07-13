'''Delpoy a backend server to AWS EC2 instance'''
import pulumi
import pulumi_aws as aws

#Create Security Group Rules
group = aws.ec2.SecurityGroup('pokemon-guesser-game-backend-server-secgrp',
    description='Enable HTTP SSH and Uvicorn access',
    #inbound rules
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0'] },
        { 'protocol': 'tcp', 'from_port': 63375, 'to_port': 63375, 'cidr_blocks': ['0.0.0.0/0']}
    ],
    #outbound rules
    egress=[ {'protocol': '-1', 'from_port': 0, 'to_port': 0, 'cidr_blocks': ['0.0.0.0/0']}])

user_data = """
#!/bin/bash
pip3 install fastapi
pip3 install uvicorn
pip3 install requests
sudo yum install -y git
git clone https://github.com/JinZhuAW/PokemonGuesserAPI.git
cd PokemonGuesserAPI
uvicorn main:app --host 0.0.0.0 --port 63375
"""
#Create ec2 instance
server = aws.ec2.Instance(resource_name='pokemon-guesser-game-backend-server',
    instance_type='t2.micro',
    tags={
        "Name": "PkmonGuesserGameAPI",
    },
    key_name='vockey',# default key pair used in the lab 
    vpc_security_group_ids=[group.id], # reference security group from above
    user_data=user_data, # reference user data from above
    ami='ami-0ca285d4c2cda3300' # default amazon machine image
    )

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
