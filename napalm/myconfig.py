#!/usr/bin/env python3
'''
Description:
    Simple script to learn functionality of the napalm library

'''
import napalm_setup

# Hard-code the switch credentials
device = napalm_setup.set_driver()
    
#Equates to: ssh into the switch, login, and enable
device.open() 
    
# Print STARTUP, RUNNING, and CANDIDATE configs 
print(device.get_config())
device.close()

