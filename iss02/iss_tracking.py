#!/usr/bin/env python3
'''
Description:
    A script for tracking the location of the ISS using API calls
    Uses turtle to display a map of the world and uses an ISS icon to display its location
    Also display the current location of seattle and the next time the ISS will pass over seattle

'''
import urllib.request
import json
import turtle
import time


def main():
    # Trace the ISS - earth-orbital space station
    eoss = 'http://api.open-notify.org/iss-now.json'

    #Call the web server
    trackiss = urllib.request.urlopen(eoss)

    #Put into file object
    track = trackiss.read()

    #JSON -> python data structure
    result = json.loads(track.decode('utf-8'))

    #Display data
    print("\n\nConverted python data")
    print("result")
    input("\nISS data retrieved & converted. Press any key to continue")

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print("\nlatitude: ", lat)
    print("\nlongitude: ", lon)

    make_screen(lon, lat)

def make_screen(lon, lat):
    #Create the screen and set the size
    screen = turtle.Screen()
    screen.setup(720, 360)

    screen.setworldcoordinates(-180, -90, 180, 90)

    #Set the map as the background
    screen.bgpic('iss_map.gif')
    #Create a new icon out of the ISS gif image
    screen.register_shape('spriteiss.gif')

    iss = turtle.Turtle()
    iss.shape('spriteiss.gif')
    iss.setheading(90)

    lon = round(float(lon))
    lat = round(float(lat))

    iss.penup()
    iss.goto( lon, lat)
    #Call the my_loc function to set the location of seattle coords
    my_loc(47.6, -122.3)

    #Lets the user reload the screen until they want to quit
    choice = ""
    while not choice:
        choice = input("Reload map [Y/n]: ").lower()
        if choice != "y":
            choice = True
        else:
            screen.clear()
            main()


def my_loc(lat, lon):

    #Setting for Seattle location marker
    yellowLat = 47
    yellowLon = -122
    my_location = turtle.Turtle()
    my_location.penup()
    my_location.color('yellow')
    my_location.goto( yellowLon, yellowLat)
    my_location.dot(5)
    my_location.hideturtle()


    #Get the next time the ISS will pass over our location
    passiss = 'http://api.open-notify.org/iss-pass.json'
    passiss = passiss + '?lat=' + str(yellowLat) + '&lon=' + str(yellowLon)
    response = urllib.request.urlopen(passiss)
    result = json.loads(response.read())

    ##print(result) ## uncomment to see the downloaded result
    over = result['response'][1]['risetime']
    style = ('Arial', 6, 'bold')
    my_location.write(time.ctime(over), font=style)


main()
