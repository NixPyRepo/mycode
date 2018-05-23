#!/usr/bin/env python3
#Author: Nick Mahoney
#Description:
#Read a log file and count the number of failed login attempts
#when a failed login is found print the IP address
#Also look for successful logins and print the number found

loginFail = 0 
loginSucc = 0

#open the keystone file in read mode
keystone = open('/home/student/mycode/parser/keystone.common.wsgi', 'r')

#create an empty list
failed_list = []

#read the lines and them to a variable
keystone_lines = keystone.readlines()

#loop over keystone_lines looking for successful and failed logins
for i in range(len(keystone_lines)):
	
	if "- - - - -] Authorization failed" in keystone_lines[i]:
		#increment failed logins
		loginFail += 1
		
		#split the failed logins at every space
		failedIP  = keystone_lines[i].split(" ")
		
		#The ip address is at the end of the line, get the last array item and appened it to the list
		failedIP  = failedIP[(len(failedIP)-1)]
		failed_list.append(failedIP)
	elif "Loaded 2" in keystone_lines[i]:
		loginSucc += 1	
		

print("\nThe number of successful logins: " + str(loginSucc))
print("\nThe number of failed logins: " + str(loginFail) + "\n")
for n in failed_list:
	print("Failed login from: " + str(n))
