#!/usr/bin/python

#primary numbers calculation
#./test.py

#Outer loop to execute
for i in range(2, 12):
    j = 2

#Inner loop to execute
    for j in range(2, (i/j)):

#execute if conditon for modulo, if modulo is zero if condition become true 
#it will brek the inner loop and iterates the 1st loop.
#if modulo is non zero condition become false and if condition execute
       if not(i%j): break

#printing prime number
    if ( j > (i/j)):
        print i, "is a prime number"
