#!/usr/local/bin python3

my_list = ["192.168.0.5", 5060, "UP"] #created a list of mixed datat types (strings and integer)

print("The first item in the list (IP): " + str(my_list[0])) #Arrays start at zero, to print the first item in the list called the my_list variable with the item at the first position to be safe cast all items as str

print("The second item in the list (port): " + str(my_list[1])) #Printing the second item in my_list and cast as str since the second item is an integer

print("The last item in the list (state): " + str(my_list[2])) #print the third and last item in my_list and cast as str

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"] #created a second list with mixed data types again


##print a message while calling various items from the list. All items are casted as str.
print("When I ssh into ip addresses " + str(new_list[3]) + " or " + str(new_list[4]) + " I am unable to ping ports " + str(new_list[0]) + ", " + str(new_list[1]) + ", or " + str(new_list[2]) + ".")