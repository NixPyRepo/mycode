#!/usr/bin/env python3
'''
Description:
    use a yaml file to validate config settings
'''

import napalm_setup
import pprint as pp

#Call in the arguments and set variables
args = napalm_setup.add_args()
os = args.operating_system
user = args.user
passwd = args.passwd
device_addr = args.addr

#Create the device object and pass in parameters
device = napalm_setup.set_driver(os, user, passwd, device_addr)


file_path = input("Enter the full path and name of the compliance file: ")
pp.pprint(device.compliance_report(file_path))
device.close()


