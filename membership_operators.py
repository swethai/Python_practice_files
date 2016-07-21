#!/usr/bin/python


a = 10 
b = 20

list = [1, 2, 3, 4, 5]

if ( a in list ):
    print "a is available in the given list"
else:
    print "a is not available in the given list"


if ( b not in list):
    print "b is not available in the list"
else:
    print "b is available in the list"


a = 2

if ( a in list ):
    print "a is available in the list"
else:
    print "a is not available in the list"


