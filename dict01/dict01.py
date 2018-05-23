#!/usr/local/bin python3
#Author: Nick Mahoney
#Description: Working with dictionaries and adding key value pairs


switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print( switch['hostname'] )
print( switch['ip'] )

## request a 'fake' key
# print( switch['lynx'] )

## request a 'fake' key with .get() method
print( "First test - .get()" )
print(switch.get('lynx'))

print( "Second test - .get()" )
print(switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!"))

print( "Third test - .get()" )
print(switch.get('version'))

print( "Fourth test - .keys()" )
print(switch.keys())

print( "Fifth test - .values()" )
print(switch.values())

print(switch.get('sw1'))