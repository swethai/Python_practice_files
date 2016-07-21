#!/usr/bin/python

def ReturnValue(*variableTuple):
    'Adds the values and return the total'
    total = 0
    for arg in variableTuple:
        total += arg
    print "total in the function", total
    return total

total = ReturnValue(10, 20, 30, 40)
print "total out side the function", total
