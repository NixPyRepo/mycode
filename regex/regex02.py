#!/usr/bin/env python3


import urllib.request
import re
import argparse
import ssl


def get_args():
    parse = argparse.ArgumentParser()
    parse.add_argument("-s", "--search", help="The key word you want to search for. To use a list of words separate with a comma(,) and NO space")
    parse.add_argument("-u", "--url", help="The url you want to search")
    args = parse.parse_args()
    return args

def web_connection(argument):

    address = argument.url

    cert = ssl.create_default_context()
    cert.check_hostname = False
    cert.verify_mode = ssl.CERT_NONE

    request = urllib.request.urlopen(address, context=cert)
    data = request.read().decode('utf-8')

    return data

def main():

    arg = get_args()
    key_word = arg.search
    web_data = web_connection(arg)

    #Used if a user supplies more than one word.
    if "," in key_word:
        key_word = key_word.split(",")

        #Search for each word in the list
        for word in key_word:
            if re.search(word.strip(), web_data):
                print("The word " + word +" was found\n")
            else:
                print("The word " + word + " could not be found\n")
    else:
        if re.search(key_word, web_data):
            print("The word " + key_word + " was found\n")
        else:
            print("The word " + key_word + " could not be found\n")

main()