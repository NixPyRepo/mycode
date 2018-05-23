#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: get an ip address from user and check "if" it matches DNS or Gateway IP

#Set gateway and dns ps in a dictionary for easy change later
bad_IPs = {"gateway": "10.10.3.1", "dns_server": "10.20.5.2"}

#Create an empty list to add IPs to
ip_list = []

#Create the ipTester function to be used later
def ipTester():

    #Get user supplied IP address
    user_ip = input("\nPlease enter an IP address or \"Q\" to quit: ")

    #loop over the dictionary to check for invalid ips
    for key, value in bad_IPs.items():

        #if an invalid IP is enter display error message and prompt for new IP
        if user_ip == value:
            print("\nThis is the " + key + " IP address. Choose a different IP address")

            #sets user_ip to different string. This keeps the bad_ips from being added to the list
            user_ip = "bad_ip"

    #As long as the ip is valid and the quit key is not entered the user supplied data will be added to the list
    if user_ip != "bad_ip" and user_ip.upper() != "Q":
        ip_list.append(user_ip)

    #Return the data in the user_ip variable to be checked in the while loop
    return user_ip

#create an empty variable for user input
choice = ""

#Loop will continue to gather IPs, until the user enters "Q"P
while choice.upper() != "Q":

    #Start the program by calling the ipTester functions and add the return value to choice
    choice = ipTester()

#When finished print the list of ips entered
print("\nThe IPs in the list are: ")

for i in ip_list:
    print(i)


