#!/usr/bin/env python3


from sys import argv
import paramiko, pmiko

user = pmiko.get_user()
passwd = pmiko.get_pass()
cmd = pmiko.get_cmd()


addr = ""
client = paramiko.SSHClient()


user_ips = {"john" : "10.10.1.2",
            "paul" : "10.10.1.3",
            "george" : "10.10.1.4",
            "stuart" : "10.10.1.5",
            "pete" : "10.10.1.6",
            "ringo" : "10.10.1.7",
            "student" : "localhost"
            }
#Set up the ssh client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())

#Establish the connection
try:
    if user in user_ips.keys():
        addr = user_ips[user]
except KeyError:
    print("The user " + user + " is not valid")


client = pmiko.start_conn(addr, user, passwd)

result = pmiko.run_command(client, cmd)

print("Result: " + result)

for line in result:
    print( " " + line.strip("\n"))








