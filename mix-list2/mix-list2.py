#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: This lab is designed to create and manipulate lists

proto = ["ssh", "http", "https"] #assign the data in square brackets to proto variable
protoa = ["ssh", "http", "https"]


print(proto)
print(proto[1]) #print the second item in the proto array

proto.append("dns") #add the string dns to the end of proto array
protoa.append("dns")

print(proto)
print(protoa)

proto2 = [22, 80, 443, 53] #create a new list with port numbers

proto.extend(proto2) #extend will iterate over the proto2 list and add each item to the proto list
protoa.append(proto2) #append will add the proto2 list as a single item to the protoa list

print(proto)
print(protoa)


proto.insert(1, "telnet") #insert a new string at a specified position
print(proto)

protoa.remove("dns") #remove the first occurance of the given string
print(protoa)