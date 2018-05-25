#!/usr/bin/env python3
#Author: Nick Mahoney
#Description:
#Using the os library to send icmp packets and pass arguments from the command line


import os
import sys


def icmp_func(count, ip):
	response = os.system("ping -c " + count + " " + ip)
	return response

print(icmp_func(sys.argv[1], sys.argv[2]))

