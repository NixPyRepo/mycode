#!/usr/bin/env python3

import urllib.request
import json
import ssl
import argparse



#Add arguments with switches
def add_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-k", "--key", help="The full path and name of the file with your API key. \n\t Example: /home/foo/barr.txt", required=True )

    parser.add_argument("-u", "--url", help="The full url name of the site you want to call\n\t Example: https://api.nasa.gov/neo/rest/v1/feed?&api_key", \
    default="https://api.nasa.gov/neo/rest/v1/feed?&api_key")

    parser.add_argument("-d", "--start_date", help="The start date in yyyy-mm-dd format", required=True)

    parser.add_argument("-D", "--end_date", help="The end date in yyy-mm-dd format")

    args = parser.parse_args()

    return args
#Create the neo object
def get_info():
    args = add_args()

    #Get api key, store it and close the file
    fileName = args.key
    readIn = open(fileName, "r")
    key = "&api_key=" + str(readIn.read())


    start_date = 'start_date=' + str(args.start_date)
    end_date = '&end_date=END_DATE'

    if args.end_date:
        end_date = '&end_date=' + str(args.end_date)

    #Create full url with api key
    neo_url = args.url + start_date + key


    #Ignore badd ssl certificate
    cert = ssl.create_default_context()
    cert.check_hostname = False
    cert.verify_mode = ssl.CERT_NONE

    neo_req = urllib.request.urlopen(neo_url, context=cert)
    neo_read = neo_req.read()
    neo_json = json.loads(neo_read.decode('utf-8'))
    return neo_json

#convert miles into moon lengths
def moon_lengths(miss_distance):

    #The number of miles in a moon length
    moon_len = 238900
    total_moon = miss_distance / moon_len
    return total_moon


neo = get_info()

for key in neo['near_earth_objects'].keys():
    date = key
    name = neo['near_earth_objects'][key][0]['name']
    hazardous = neo['near_earth_objects'][key][0]['is_potentially_hazardous_asteroid']

    #Set appropriate message based on true/false value
    if not hazardous:
        hazardous = "potentially hazardous"
    else:
        hazardous = "harmless"

    print("On " + str(date) + " there was a " + hazardous + " near\nearth object named " + name + ", that missed by: \n")
    miss_miles = int(neo['near_earth_objects'][key][1]['close_approach_data'][0]['miss_distance']['miles'])
    print("Miles: " + str(miss_miles))

    total_miss = round(moon_lengths(int(miss_miles)))
    print("Moon lengths: " + str(total_miss) + "\n") #+ str(moon_lengths(miss_miles)) + "\n")
