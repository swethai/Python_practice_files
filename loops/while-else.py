#!/usr/bin/python

#while loop with else
#./test.py

count = 0

#while else loop, if while loop condition fails else will executes.
while ( count < 5 ):
    print count, "is less than 5"
    count = count + 1
else:
    print "count is not less than 5"

print "Good bye!"
