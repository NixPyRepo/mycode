#!/usr/bin/env python3

import random
import turtle
from time import sleep
SIZE = 100

def make_screen(width, height):
    screen = turtle.Screen()
    screen.setup(width, height)

    #screen.setworldcoordinates(-180, -90, 180, 90)

#Settings for the dice object
def draw_dice(size):

    dice = turtle.Turtle()
    dice.speed(0)
    dice.hideturtle()
    return dice

def dice_1(dice, size):
    dice.penup()
    dice.goto(0,0)
    dice.dot(20, 'red')

def dice_2(dice, size):
    dice.penup()
    dice.goto(size/-4, size/4)
    dice.dot(20, 'red')
    dice.penup()
    dice.goto(size/4, size/-4)
    dice.dot(20, 'red')

def dice_3(dice, size):
    dice_1(dice,size)
    dice_2(dice, size)

def dice_4(dice, size):
    dice.penup()
    dice.goto(size/-4, size/-4)
    dice.dot(20, 'red')
    dice.penup()
    dice.goto(size/4, size/4)
    dice.dot(20, 'red')
    dice_2(dice, size)

def dice_5(dice, size):
    dice_1(dice, size)
    dice_4(dice, size)

def dice_6(dice, size):
    dice_4(dice, size)
    dice.penup()
    dice.goto(size/-4, 0)
    dice.dot(20, 'red')
    dice.penup()
    dice.goto(size/4, 0)
    dice.dot(20, 'red')

#Used for the animation to roll the dice
def roll_dice():
    turtle.shape('square')
    turtle.shapesize(5,5)
    turtle.speed(1)

    for i in range(2):
        turtle.tilt(45)
        sleep(.3)

def get_players():
    #Error handling for bad input
    try:
        num_players = int(input("How many players are there?: "))

    except ValueError:
        num_players = int(input("You did not enter a valid number\n"))


    #Empty dictionary to hold player/score items
    player_dict = {}

    #Get user names
    for i in range(1, (num_players + 1)):
        player_dict[input("Enter name for player " + str(i) + ": ")] = []

    return player_dict

#Put each side of the dice into a dictionary.
#If the function was put into the dictionary it
#would have called each function as the dictionary
#was being built.
dice_dic = {1: dice_1,
            2: dice_2,
            3: dice_3,
            4: dice_4,
            5: dice_5,
            6: dice_6
            }

players = get_players()

#set the rounds var
count = 0
try:
    turns = int(input("\nHow many rounds would you like to play?: "))
except ValueError:
    turns = int(input("You did not enter a number. Please enter the number of rounds you would like to play: "))

make_screen(400, 400)

#Loop to do three rounds
while count < turns:

    #Clear the dice off the screen
    turtle.Screen().clearscreen()


    for key in players.keys():
        roll = input("\nIt's " + key + "s turn. press any key to roll the dice")

        #Get a random number between 1-6
        roll_num = random.randint(1, 6)
        roll_dice()

        dice = draw_dice(SIZE)
        dice_dic[roll_num](dice, SIZE)
        input(key + " rolled a " + str(roll_num) + ". Press enter to continue")

        #Add the number rolled to the players scored
        #An empty list cant be iterated. The first roll for each player will simply set the value
        if count == 0:
            players[key] = int(roll_num)
        #With at least one value in the list we can now add the scores
        else:
            #score = int(players[key])
            players[key] += int(roll_num)

    #Increment the rounds var
    count += 1

print("\n\n" + "*" * 10 + " RANKING " + "*" * 10)

#Sorts the value from highest to lowest
for k in sorted(players, key=players.get, reverse=True):
    print(k + " with " + str(players[k]) + " points")


