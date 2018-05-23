#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: get an ip address from user and check "if" it matches DNS or Gateway IP

#Set gateway and dns variables for easy change later
gateway = "10.10.3.1"
dns_server = "10.20.5.2"

#Create an empty list to add IPs to
ip_list = []

#Create the ipTester function to be used later
def ipTester():

    user_ip = input("\nPlease enter an IP address: ") #Get user supplied IP address

    #Check user_ip against gateway and dns_server. if true re-prompts for new ip address
    if user_ip == gateway:
        print("\nThis is the Gateway IP address. Please choose another IP address")
        ipTester()
    elif user_ip == dns_server:
        print("\nThis is the DNS server IP address. Please choose another IP address")
        ipTester()
    else:#If the user supplied IP does not match GW or dns_server add it to a list
        ip_list.append(user_ip)


user_answer = "" #create an empty variable for user input

while user_answer != "Q": #Loop will continue to gather IPs, until the user enter "Q"

    ipTester() #tStart the program by calling the ipTester functions
    user_answer = input("\nTo quit press \"Q\" or Enter to continue").upper() #Confirm if user want to quit or continue and store it as upper case

#When finished print the list of ips entered
print("\nThe IPs in the list are: ")
for i in ip_list:
    print(i)


