#!/usr/bin/env python3
'''
Description:
    use a yaml file to validate config settings
'''

import napalm_setup
import pprint as pp

device = napalm_setup.set_driver()
file_path = input("Enter the full path and name of the complaince file: ")
pp.pprint(device.compliance_report(file_path))
device.close()


