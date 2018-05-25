#!/usr/bin/env python3
#Description:
#use a yaml file to validate config settings


from napalm import get_network_driver
import sys
import pprint as pp

driver = get_network_driver('eos')
device = driver('172.16.2.10', sys.argv[1], sys.argv[2])
device.open()


file_path = input("Enter the full path and name of the complaince file: ")
pp.pprint(device.compliance_report(file_path))


