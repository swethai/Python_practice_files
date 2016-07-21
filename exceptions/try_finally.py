#!/usr/bin/python

#Try, finally 
#python test.py

#try bock
try:
    fo = open('foo.txt', 'w')
    fo.write('swetha')

#finally block, must executes
finally:
    print " finally Block:"
    print "must execute block, irrespective of error or not"
