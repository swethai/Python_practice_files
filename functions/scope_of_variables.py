#!/usr/bin/python

#scope of the variable
#python test.py

#declaring the gloabal variable
total = 0

#declaring the function
def ScopeOfVariables(arg1, arg2):
    'Adds the two arguments'
    total = arg1 + arg2
    print "total value is : ", total
    return total;

#calling the function
ScopeOfVariables(10, 20)
print "total outside the function is : ", total

