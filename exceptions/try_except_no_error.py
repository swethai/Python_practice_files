#!/usr/bin/python

#Exception handling with no errors
#python test.py

#try block
try:
    fo = open('foo.txt', 'w')
    fo.write("swetha");

#Exception block, executes if exception occured
except IOError:
    print "Error: can not find file or read data"

#Executes if no exception occured
else:
    print "Written content to the file succesfully"



