#!/usr/bin/env python3
'''
Description:
    Reload configs to remote device from a text file
'''


import napalm_setup

#Call in the arguments and set variables
args = napalm_setup.add_args()
os = args.operating_system
user = args.user
passwd = args.passwd
device_addr = args.addr

#Create the device object and pass in parameters
device = napalm_setup.set_driver(os, user, passwd, device_addr)

file_path = input("Enter the full path and name of the file?: ")
device.load_replace_candidate(filename=file_path)

print(device.compare_config())
device.commit_config()
device.close()



