#!/usr/bin/env python3

from datetime import datetime # required to use datetime
startTime = datetime.now()    # returns the time of right now from the datetime object
# Note that datetime is an object, not a simple string.

## WRITE YOUR OWN CODE TO DO SOMETHING. ANYTHING.
# SUGGESTION: Replace with code to print a question to screen and collect data from user.
# MORE DIFFICULT -- Place the response(s) in a list & continue asking the question until the user enters the word 'quit'


## Explore the statrTime object
print('The startTime hour is: ' + str(startTime.hour))
print('The startTime minute is: ' + str(startTime.minute))
print('The startTime day is: ' + str(startTime.day))
print('The startTime year is: ' + str(startTime.year))

#Create empty list top hold the words
user_words = []


user_choice = ""

#Keep asking questions until the user presses "q"
while user_choice != "q":

    user_choice = input("Enter a word to add to the dictionary or press \'q'\' to quit: ")

    if user_choice.lower() != "q":
        user_words.append(user_choice)

print("You entered " + str(len(user_words)) + " words and they are: ")
#Print each word individualy
for word in user_words:
    print(word)




## Figure out how long it took to do that something
print('\nThe code took: ' + str(datetime.now() - startTime) + ' to run.')


