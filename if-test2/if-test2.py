#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: Working with if statements to validate IPv4 addresses

def check_ip():
    ip_check = input("Apply an IP address: ") #get user input and assign it to ip_check

    gateway = "192.168.70.1"

    if ip_check == gateway:
        print("Looks like the IP address of the gateway was set: " + ip_check + " this is not recommended.\n")
        answer = input("Do you want to continue (Y/N)?: ").upper()

        if answer == "N":
            check_ip()


    elif ip_check: #check to see if ip_check is true (not empty)
        print("Looks like the IP address was set: " + ip_check + "\n")

    else:
        print("You did not enter input \n")
        check_ip()

check_ip()
print("The program is now exiting")
