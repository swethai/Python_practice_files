#!/usr/bin/python

#Dictionary program
#./test.py

#declaring the dictionary
dict = {}

#Assing key value pair to dictionary
dict['one'] = 'this is one'
dict[2] = 'this is two'

dict1 = {'name': 'swetha', 'code': 12345, 'dep': 'sales'}

#prints value of mentioned keys
print dict['one']
print dict[2]

#prints complete dictionary
print dict1

#prints value of 'code' key
print dict1['code']

#prints keys of dictionary
print dict1.keys()

#prints values of dictionary
print dict1.values()

