#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: Using if/elif statements to print letter grade from user supplied numeric score

def letterGrade():#Define the function to convert numeric score to letter grade

    user_score = float(input("Please enter your numeric score: "))#Get user supplied data and stores it as a float

    #Ensure user supplied data is in the correct range if not, the function will start over
    if user_score >= 0 and user_score <= 100:

        #A series of if/elif statements to check the user supplied data. When statment evaluates to true the corresponding message will print
        if user_score >= 90:
            print("Based on your score of " + str(user_score) + " your letter grade is: A")
        elif user_score <= 89.9 and user_score >= 80:
            print("Based on your score of " + str(user_score) + " your letter grade is: B")
        elif user_score <= 79.9 and user_score >= 70:
            print("Based on your score of " + str(user_score) + " your letter grade is: C")
        elif user_score <= 69.9 and user_score >= 60:
            print("Based on your score of " + str(user_score) + " your letter grade is: D")
        else:
            print("Based on your score of " + str(user_score) + " your letter grade is: F")
    else:
        print("You must enter a number between 0 and 100\n")#Prints error message
        letterGrade()

    user_answer = input("Would you like to try another score (Y/N)?: ").upper() #Lets the user enter additional scores

    if user_answer == "Y" or user_answer == "YES":
        letterGrade()
    else:
        print("The program will now close")

letterGrade() #Start the program by calling the function
