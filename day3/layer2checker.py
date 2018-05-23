#!/usr/bin/env python3
#Author: Nick Mahoney
#Description: prompts the user for an L2 protocol and loops until a valid L2 protocol is entered

#Add L2 protocols and message into a dictionary
l2Proto = {"eth": "ethernet protocol allowed",
           "fc": "fiber channel NOT allowed",
           "ifb": "infiniband NOT allowed",
           "otn": "optical network allowed"}

#
user_proto = ""
while (user_proto not in l2Proto.keys()):

    user_proto = input("Enter your L2 protocol: ")

    if user_proto in l2Proto.keys():
        print(l2Proto[user_proto])

    else:
        print("no idea what technology that is\n")
