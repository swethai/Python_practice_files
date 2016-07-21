#!/usr/bin/pythopn

#exception handling with error
#python test.py

#try block, executes actual code
try:
    fo = open('foo1.txt', 'r')
    fo.read()

#if any exception occured in the try block except block executes
except IOError:
    print "Can not read data from file"

#else block will executes if no exception occured
else:
    print "Data read successfully"
