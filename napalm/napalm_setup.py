#!/usr/bin/env python3

import argparse
from napalm import get_network_driver


# add cmd line arguments
def add_args():
    arguments = argparse.ArgumentParser()

    arguments.add_argument("-O", "--operating_system", help="The OS of the device you want to connect to",
                           default="eos")
    arguments.add_argument("-u", "--user", help="The user name to login with", required=True)
    arguments.add_argument("-p", "--password", help="The password to login with", required=True)
    arguments.add_argument("-a", "--address", help="The address (IP/hostname) of the device you want to connect to",
                           required=True)
    args = arguments.parse_args()
    return args

def set_driver():

    # Setting
    args = add_args()
    os = args.operating_system
    user = args.user
    passwd = args.password
    addr = args.address

    # Choose the device driver to use, Arista in this example
    driver = get_network_driver(os)

    # Set device info, IP address, user name, and password
    device = driver(addr, user, passwd)
    device.open()

    return device

