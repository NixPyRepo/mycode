#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: Working with if statements & user input

hostname = input("Please enter the hostname: ").upper() #get input from user, convert the string to upper case, and store it in the hostname variable

if hostname == "MTG": #if statement to see if the hostname variable matches the expected string, if true print the below
    print("The hostname was found to be " + hostname)
    print("The hostname matches expected config")

print("Program is exiting") #let the user know the program is finished


