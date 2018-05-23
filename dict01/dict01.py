#!/usr/local/bin python3
#Author: Nick Mahoney
#Description:


## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print(switch['hostname'])
print(switch['ip'])

## request a 'fake' key
print(switch['lynx'])