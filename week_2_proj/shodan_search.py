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
    argument.add_argument('-t', '--target', help='The IP address of the device you want to query in shodan')
    argument.add_argument('-v', '--verbose', help='Get all the information printed from the query', action="store_true")
    argument.add_argument("-sC", "--source", help='Source you want to query (ExploitDB, CVE, Metasploit)')
    argument.add_argument("-p", "--platform", help='The operating system you want to use (Linux, Windows, osx)')
    argument.add_argument("-s", "--search", help='The the search phrase you want to enter. i.e. Cisco, Apache, FTP')
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

    #If nor records were found
    if "error" in r.json().keys():
        print("\n" + ">"*8 +"Target: " + ip + "<"*8)
        print(r.json()['error'])

    #If the -v option is not used, print basic informatio
    elif not verbose:
        #Create variables for basic information
        domain = r.json()['data'][0]['domains']
        hostnames = r.json()['hostnames']
        org = r.json()['org']
        country = r.json()['country_name']
        ports = r.json()['ports']

        print("\n" + ">"*8 + " Target: " + ip + " " + "<"*8)
        print("Domain: " + str(domain))
        print("Hostnames: " + str(hostnames))
        print("Organization: " + str(org))
        print("Country: " + str(country))
        print("Ports: " + str(ports))
    #When the -v option is used print all the information
    else:
        print("\n" + ">"*8 + " Target: " + ip + " " + "<"*8)
        pprint.pprint(r.json())



def my_ip(key):

    url = "https://api.shodan.io/tools/myip?key="
    r = requests.get(url)

    return r.json()

def get_exploit(key, platform, source, search):

    #Create api search string. %3A are colons
    source = "+source%3A" + source
    platform = "+platform%3A" + platform
    key = "&key=" + key

    url = "https://exploits.shodan.io/api/search?query=" + search + source + platform + key
    r = requests.get(url)
    vulns = r.json()

    if not verbose:
        #For each CVE/Vuln found print our the description and CVE number
        print("\n" + "*"*8 + "Found: " + str(vulns['total']) + " vulnerabilities for " + search + "*"*8)
        for i in range(len(vulns['matches'])):
            #Error handling for missing cve number
            try:
                cve = str(vulns['matches'][i]['cve'])
                print("CVE: " + cve)

            except KeyError:
                print("CVE: None")

            descrip = str(vulns['matches'][i]['description'])

            print("Description: " + descrip + "\n")
    else:
        pprint.pprint(vulns)




arg = add_args()
key = load_key(arg.key)
verbose = arg.verbose
ip = arg.target
base_url = "https://api.shodan.io/"
os_platform = arg.platform
database = arg.source
search_string = arg.search

#Example dns info
#dns_info(key, ip, verbose, base_url)

#Example exploit query
#get_exploit(key, os_platform, database, search_string)

