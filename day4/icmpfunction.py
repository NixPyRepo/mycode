#!/usr/bin/env python3
#Author: Nick Mahoney
#Description:
#Create a function that take two arguments from the user and passes them into the function
#The function will execute a ping -c X X.X.X.X command with the given arguments


from subprocess import call

def icmp_call(count, ip):

	print("/n>>>>>Sending icmp packets to " + str(ip) + "<<<<<\n")	
	call(["ping", "-c", count, ip])

user_count = input("Enter the number of pings to send: ")
user_ip = input("Enter the IP address to ping: ")

icmp_call(user_count, user_ip)


