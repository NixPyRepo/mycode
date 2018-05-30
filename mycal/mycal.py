#!/usr/bin/python
'''
Author: Nick Mahoney
Description:
    use calendar and datetime to print each month in th year with a loop
    and find the next leap year
'''

import calendar
import datetime


#A loop to call each month of the year and print the calendar
for i in range(1,13):
    lilcal = calendar.month(2018, i)
    print("\n\nHere is a tiny calendar:")
    print(lilcal)


#Set the current year
year = int(datetime.date.today().strftime("%Y"))

#Continue to loop until a leap year is found
while not calendar.isleap(year):

    if year == int(datetime.date.today().strftime("%Y")):
        print(str(year) + " is not a leap year\n")

    #Incfement the year
    year += 1

print("The next leap year is " + str(year))
