#!/usr/bin/env python3
'''
Author: Nick Mahoney
Description:
    Using NASA api to get the picture of the day.
    Print the Title, Date, and explanation of the image and allow user to download it.
    curl is used to download the image and save in current working directory.

    Usage:
        nasa_api01.py -k /home/foo/bar.txt -u https://api.nasa.gov/planetary/apod?api_key=
'''




import urllib.request
import json
import webbrowser
import ssl
import argparse
from subprocess import call


#Add arguments with switches
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--key", help="The full path and name of the file with your API key. \n\t Example: /home/foo/barr.txt", required=True )
parser.add_argument("-u", "--url", help="The full url name of the site you want to call\n\t Example: https://api.nasa.gov/planetary/apod?api_key=", required=True)
args = parser.parse_args()

#Get api key, store it and close the file
fileName = args.key
readIn = open(fileName, "r")
key = str(readIn.read())


#Ignore badd ssl certificate
cert = ssl.create_default_context()
cert.check_hostname = False
cert.verify_mode = ssl.CERT_NONE



#Combine key and url for full api call
apod_url = args.url + key

#Open rad and store url response in json format
apod_open = urllib.request.urlopen(apod_url, context=cert)
apod_read = apod_open.read()
apod_json = json.loads(apod_read.decode('utf-8'))


print("Title: " + str(apod_json['title']))
print("Date: " + str(apod_json['date']))
print("Explanation: " + str(apod_json['explanation']))

input("\nPress any key to open the image in browser: ")
webbrowser.open(apod_json['url'])

download = input("\nWould you like to download the picture? [Y/n]: ").lower()
answers = ["y", "yes", "n", "no"]

while download not in answers:
    download = input("\nWould you like to download the picture? [Y/n]: ").lower()

if download == answers[0] or download == answers[1]:
    picture_name = "HD_" + apod_json['title']+".jpg"
    #Download the image with curl and save to picture_name file with "-o" option
    call(['curl', apod_json['hdurl'], "-o", picture_name])












