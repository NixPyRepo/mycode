#!/usr/bin/env python3
'''
Author: Nick Mahoney
Description:
    Use napalm to query remote devices for configurations
    import napalm setup script to add arguments and create driver object
'''

import pprint as pp
import napalm_setup

#Call in the arguments and set variables
args = napalm_setup.add_args()
os = args.operating_system
user = args.user
passwd = args.passwd
device_addr = args.addr

#Create the device object and pass in parameters
device = napalm_setup.set_driver(os, user, passwd, device_addr)

device.get_facts()
pp.pprint(device.get_facts())
config = device.get_config()

#get the running config of the device
running_conf = config['running']

print(running_conf)

path = '/home/student/sw1.conf'

sw1_conf_file = open(path, 'w')
sw1_conf_file.write(running_conf)
sw1_conf_file.close()
device.close()


