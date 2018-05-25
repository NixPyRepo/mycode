#!/usr/bin/env python3
#Author: Nick Mahoney
#Description:
#Take file name and path as arguments, open the file and add tabs to each line


import sys
import os

#Command line arguments for filename and path name
file_name = sys.argv[1]
path_name = sys.argv[2]

#Search for file name
for root, dirs, files in os.walk(path_name):
    if file_name in files:
        file_name = os.path.join(root, file_name)

#Open file in read mode
file_list = open(file_name, "r")

print("\t".join(file_list))
