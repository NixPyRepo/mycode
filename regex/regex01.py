#!/usr/bin/env python3
'''
Author: Nick Mahoney
Description:
    makr url request to find IP address and validate with regex.
    Then return the ip address in a print function
'''


import urllib.request
import re
import netifaces

def get_external_ip():
    #Website that returns public IP address
    url = "http://checkip.dyndns.org"

    #Call the website and read the information into the variable
    requesty = urllib.request.urlopen(url).read().decode('utf-8')

    #Regex to validate IP
    external = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', requesty)

    return external


def get_lan_ip():

    #Get interfaces
    print("\n" + ">"*8 + " Available interfaces " + "<"*8)
    print(netifaces.interfaces())
    iface = input("\nEnter the interface you want the IP address for: ")

    #Gets the ip address specific to the interface choosen
    return (netifaces.ifaddresses(iface)[netifaces.AF_INET])[0]['addr']

public = str(get_external_ip())
private = str(get_lan_ip())

print("\n\nYour public IP address is : " + public)
print("Your private IP address is : " + private)

