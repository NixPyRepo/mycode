#!/usr/bin/env python3
#Author: Nick Mahoney
#Description:
#Read a log file and count the number of failed login attempts
#when a failed login is found print the IP address
#Also look for successful logins and print the number found

import os


file_name = "keystone.common.wsgi"
#Set the path to look for the file
path_name = "$HOME"

#us the os walk method to search for the file in the home dir
for root, dirs, files in os.walk(path_name):

	#once found join the root path with the filename to create the full path
	if file_name in files:
		file_name = os.path.join(root, file_name)

loginFail = 0 
loginSuccess = 0

#open the keystone file in read mode
keystone = open(file_name, 'r')

#create an empty list
failed_list = []

#read the lines and them to a variable
keystone_lines = keystone.readlines()

#loop over keystone_lines looking for successful and failed logins
for i in range(len(keystone_lines)):
	
	if "- - - - -] Authorization failed" in keystone_lines[i]:
		#increment failed logins
		loginFail += 1
		
		#split the failed logins at every space and get the last item in the split list
		failed_list.append(keystone_lines[i].split(" ")[-1])
		
	elif "Loaded 2" in keystone_lines[i]:
		loginSuccess += 1
		
keystone.close() 
print("\nThe number of successful logins: " + str(loginSuccess))
print("\nThe number of failed logins: " + str(loginFail) + "\n")
for n in failed_list:
	print("Failed login from: " + str(n))
