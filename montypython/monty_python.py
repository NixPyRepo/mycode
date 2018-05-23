#!/usr/bin/env python3
#Author: Nick Mahoney
#Description: Using a while loop have a user try and guess the title of the monty python movie
#             if the user guesses incorrect have a count keep track of the attempt number
#             the loop should continue until the user enter the correct answer "Brian" or secret answer "shruberry"

#counter to keep track of attempts
round = 0

#dictionary to hold correct answers
answers = {"brian": "Correct", "shruberry": "You gave the super secret answer!"}

user_guess = ""

#While the users answer is not in the key and the round is less than 3 continue to prompt
while (user_guess not in answers.keys() and round < 3):

    #increment round
    round += 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    user_guess = input().lower()

    #The user entered the correct answer
    if user_guess in answers.keys():
        print(answers[user_guess])

    #The user hit the max attempts
    elif round == 3:
        print("Sorry the answer is " + str(list(answers.keys())[0]))

    else:
        print("Sorry, try again\n")
