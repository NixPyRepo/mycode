#!/usr/bin/env python3

import paramiko
from sys import argv







#Set up the ssh client

def start_conn(ip, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())

    #Establish the connection
    client.connect(ip, username=user, password=passwd)
    return client

#Accept argument

def get_user():
    user = argv[1]
    return user

def get_pass():
    passwd = argv[2]
    return passwd

def get_cmd():
    cmd = argv[3]
    return cmd

def run_cmd(client, command):

    stdin, stdout, stderr = client.exec_command(command)

    if stdout:
        return stdout

    else:
        return stderr




