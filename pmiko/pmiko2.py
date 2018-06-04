#!/usr/bin/env python3


import paramiko, pmiko

user = pmiko.get_user()
passwd = pmiko.get_pass()
cmd = pmiko.get_cmd()


addr = ""
client = paramiko.SSHClient()

#A dictionary to hold all users and their IPs
user_ips = {"john" : "10.10.1.2",
            "paul" : "10.10.1.3",
            "george" : "10.10.1.4",
            "stuart" : "10.10.1.5",
            "pete" : "10.10.1.6",
            "ringo" : "10.10.1.7",
            "student" : "localhost"
            }

#Establish the connection
if user in user_ips.keys():
    addr = user_ips[user]
else:
    print("The user " + user + " is not valid")


client = pmiko.start_conn(addr, user, passwd)

result = pmiko.run_command(client, cmd)

print("Result: " + cmd)

for line in result:
    print( " " + line.strip("\n"))








