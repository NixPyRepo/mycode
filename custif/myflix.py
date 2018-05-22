#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: Working with more if/elif statments to print best speed for video quality


message = 'The movie is about to begin, we recommend ' #set the message to display to the user
connection = float(input('What is your connection speed in Mbps?: ')) #Get user input and store it as a float in the connections variable

##A series of if/elif statements. Once the statment returns true the corresponding message will be printed
##Each if/elif statement reassigns the message variable to concatenate the original with the specified setting
if connection >= 25:
    message = message + 'setting video to 4k.'
elif connection >= 5:
    message = message + 'setting video to 1080p.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)