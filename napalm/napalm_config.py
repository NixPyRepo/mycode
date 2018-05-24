#!/usr/bin/env python3
#Description: 
#Use napalm to query remote devices for configurations
#and use commmand line arguments to supply login creds
from napalm import get_network_driver
import pprint as pp
import sys

#Choose the device driver to use, Arista in this example
driver = get_network_driver('eos')

#Set device info, IP address, user name, and password
device = driver('172.16.2.10', sys.argv[1], sys.argv[2])

device.open()

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


