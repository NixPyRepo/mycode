#!/usr/bin/env python3
'''
Description:
    Simple script to learn functionality of the napalm library

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
    
#Equates to: ssh into the switch, login, and enable
device.open() 
    
# Print STARTUP, RUNNING, and CANDIDATE configs 
print(device.get_config())
device.close()

