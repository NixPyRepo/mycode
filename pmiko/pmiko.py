#!/usr/bin/env python3

import paramiko
from sys import argv


#Set up the ssh client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

#Establish the connection
client.connect('localhost', username=argv[1], password=argv[2])


#Accept argument
cmd = argv[3]


def run_cmd(command):

    stdin, stdout, stderr = client.exec_command(command)

    if stdout:
        return stdout

    else:
        return stderr


result = run_cmd(cmd)

print('result ' + cmd)

for line in result:
    print(' ' + line.strip('\n'))


