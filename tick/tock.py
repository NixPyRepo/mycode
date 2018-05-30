#!/usr/bin/env python3
'''
Description:
    Use time library to manipulate time
    Given a birthday find the time someone has been alive in seconds
    Print the time 500 seconds from run time


'''
import time # This is required to include time module

## Count the number of ticks from the epoch
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970: " + str(ticks))

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print("The local time touple is: " + str(myTime))
print("The local time touple year is: " + str(myTime[0]))
print("The local time touple month is: " + str(myTime[1]))
print("The local time touple day is: " + str(myTime[2]))
print("The local time touple hour is: " + str(myTime[3]))
print("The local time touple minute is: " + str(myTime[4]))
print("The local time touple second is: " + str(myTime[5]))
print("The local time touple week is: " + str(myTime[6]))
print("The local time touple year is: " + str(myTime[7]))
print("The local time touple daylight savings is: " + str(myTime[8]))

birthday = "1986-07-16"
pattern = "%Y-%m-%d"
today = time.time()

#convert birthday into epoch time
seconds = time.mktime(time.strptime(birthday, pattern))

#Get the difference between today and birthday to determine seconds alive
diff = today - seconds
print("\n\nYou've been alive for " + str(diff) + " seconds")


#Add 500 seconds to the current time
today = time.gmtime((today + 500))
print("In 500 seconds it be " + time.strftime("%H:%M:%S", today))

#get todays date in epoch time
today = time.time()

#Add 500 days to it
today += (86400*500)


print("Human readable time in 500 days will be: " + time.ctime(today))
print("Epoch time in 500 days will be: " + str(today))



