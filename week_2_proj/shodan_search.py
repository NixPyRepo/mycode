#!/usr/bin/env python3
'''
Author: Nick Mahoney
Description:
    Using shodans API to query information on a given host, such as DNS information.
    Can also be used to find the public IP of current machine.
'''

import argparse
import pprint
import requests


def add_args():

    argument = argparse.ArgumentParser()
    argument.add_argument('-k', '--key', help='The full name and path of the file that hold he api key', required=True)
    argument.add_argument('-t', '--target', help='The IP address of the device you want to query in shodan', required=True)
    argument.add_argument('-v', '--verbose', help='Get all the information printed from the query', action="store_true")
    args = argument.parse_args()
    return args

#Open and read the api key into the api_key variable
def load_key(file_path):
    api_file = open(file_path, 'r')
    api_key = api_file.read()
    api_file.close()
    return api_key

def dns_info(key, ip, verbose, url):

    #Create the API string
    full_url = url + "shodan/host/" + ip + "?key=" + key
    #Make the API call
    r = requests.get(full_url)

    #Create variables for basic information
    domain = r.json()['data'][0]['domains']
    hostnames = r.json()['hostnames']
    org = r.json()['org']
    country = r.json()['country_name']
    ports = r.json()['ports']

    #If the -v option is not used, print basic informatio
    if not verbose:
        print("\n" + ">"*8 + " Target: " + ip + " " + "<"*8)
        print("Domain: " + str(domain))
        print("Hostnames: " + str(hostnames))
        print("Organization: " + str(org))
        print("Country: " + str(country))
        print("Ports: " + str(ports))
    #When the -v option is used print all the information
    else:
        print("\n" + ">"*8 + " Target: " + ip + " " + "<"*8)
        return pprint.pprint(r.json())




arg = add_args()
ip = arg.target
key = load_key(arg.key)
verbose = arg.verbose

base_url = "https://api.shodan.io/"
info = dns_info(key, ip, verbose, base_url)

print(info)