#!/usr/bin/env python3
'''
Description:
    Reload configs to remote device from a text file
'''


import napalm_setup

device = napalm_setup.set_driver()

file_path = input("Enter the full path and name of the file?: ")
device.load_replace_candidate(filename=file_path)

print(device.compare_config())
device.commit_config()
device.close()



