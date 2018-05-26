#!/usr/bin/env python3
#Author: Nick Mahoney
'''
Description:
    Check user supplied IP address for block of 10 IPs
    Last octect must be less than 255
'''

import sys

ip = sys.argv[1]

def check_ip(ip_addr):
    #Check for 4 octets in ip address
    while len(ip_addr.split(".")) > 4:
        ip_addr = input("You enter an invalid IPv4 address. Please enter a valid IP: ")

    #Create the max IP in the range
    ip_block = int(ip_addr.split(".")[-1]) + 10

    if ip_block > 255:
        return False
    else:
        return True

result = check_ip(ip)

if not result:
    print("Your IP address will be greater than 255")

else:
    print("Your IP address is valid")


