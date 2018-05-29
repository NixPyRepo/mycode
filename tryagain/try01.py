#!/usr/bin/env python3

try:
    name = input("Enter a file name: ")
    file = open(name, 'w')
except:
    print('Error with that file name!')
    name = input("Enter a file name: ")
    file = open(name, 'w')
finally:
    print('This code will always execute')

