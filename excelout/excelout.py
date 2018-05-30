#!/usr/bin/env python3
'''
Description:
    Writing to an excel spread sheet

    requires:
        - pyexcel
        - pyexcel-xls (xls plugin)

'''

import pyexcel
import re
import ipaddress as ip
# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IPv4 address?: ")
    input_driver = input("What is the driver associated with this device? ")
    input_mac = input("\nWhat is the MAC address of the driver?: ")
    input_gw = input("\nWhat is the default gateway of this driver?: ")

    #Check for valid IP address
    try:
        ip_val = re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", input_ip)
        if not ip_val:
            raise ValueError
        #input_driver = input("\nWhat is the driver associated with this device? ")
        #input_mac = input("\nWhat is the MAC address of the driver")
        #input_gw = input("\nWhat is the default gateway of the driver")
    except ValueError:
        print("You did not enter a valid IP address")
        input("\nWhat is the IPv4 address?: ")
    d = {"IP": input_ip, "driver": input_driver, "MAC": input_mac, "GW": input_gw}
    return d


## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}, {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name=filename)

print("The file " + filename + ".xls should be in your local directory")
