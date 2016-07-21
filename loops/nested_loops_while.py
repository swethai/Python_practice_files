#!/usr/bin/python

#Prime no. printing with nested loop
#./test.py


#Outer While condition 
i = 2
while ( i < 100 ):
    j = 2

#inner while condition
#Execute the loop till half of the value i
    while ( j <= ( i/j ) ):

#execute if conditon for modulo, if modulo is zero if condition become true 
#it will brek the inner loop and iterates the 1st loop.
#if modulo is non zero condition become false and if condition execute
        if  not(i%j) : break
        j = j + 1

#printin prime number
    if (j > (i /j)):
        print i, " is prime number"
    i = i + 1
print "Good bye!"
