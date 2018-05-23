#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: prompts the user for an L2 protocol and loops until a valid L2 protocol is entered


l2Proto = {"eth": "ethernet protocol allowed",
           "fc": "fiber channel NOT allowed",
           "ifb": "infiniband NOT allowed",
           "otn": "optical network allowed"}
user_l2 = ""
while True:
    user_l2 = input("Enter your L2 protocol: ")
    if user_l2 not in l2Proto.keys():
        print("no idea what technology that is\n")
    else:
        print(l2Proto[user_l2])
        break
