#!/usr/bin/env python3
#Description:
#Reload configs to remote device from a text file

from napalm import get_network_driver
import sys

driver = get_network_driver('eos')
device = driver('172.16.2.10', sys.argv[1], sys.argv[2])
device.open()

file_path = input("Enter the full path and name of the file?: ")
device.load_replace_candidate(filename=file_path)
print(device.compare_config())

device.commit_config()



