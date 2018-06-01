#!/usr/bin/env python3
'''
Author: Nick Mahoney
Description:
    Use napalm to query remote devices for configurations
    import napalm setup script to add arguments and create driver object
'''

import pprint as pp
import napalm_setup

#Create device object from the driver method in napalm_setup
device = napalm_setup.set_driver()

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


