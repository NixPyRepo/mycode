#!/usr/bin/env python3
#Author: Nick Mahoney
#Description:
#Use a single print statement to print the values from the dictionary with "CISCO LOGIN INFO - " infront of the value

cisco_ios = {'device_type': 'cisco_ios_ssh', 'ip': '10.10.10.27', 'username': 'admin',
             'password': 'passwd', 'port': 22}

#Iterate over the dictionary
for k, v in cisco_ios.items():

    #Print only the value from the key:value pairs
    print("CISCO LOGIN INFO - " + str(v))
