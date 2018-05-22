#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: A continuation of list manipulation lab

list1 = ["cisco_nxos", "arista_eos", "cisco_ios"] #assign the specified strings to the list1 variable & print
print(list1)

list1.extend(["juniper"]) #usig extend add the string juniper
print(list1)

list1.append(["10.1.0.1", "10.2.0.1", "10.3.0.1"]) #append only takes one value, to add multiple values in one append statement add them as a list
print(list1)
print(list1[4]) #print the newly added item
print(list1[4][0]) #print the last item in the list1 array and the first item in the list of IPs

animals = ["cat", "dog", "fox", "cow", "rat"]

for i in animals:
    print(i, end=" ")
