#!/usr/bin/python

#Printing prime numbers in between  the 10 and 20
#./test.py

#iterating between 10 to 20
for num in range(10, 20):

#iterating between 2 to num
    for i in range(2, num):

#To determine the first factor
        if num%i == 0:

#To determine the second factor
            j=num/i
            print '%d equals %d * %d' %(num, i, j)
#To move to the next numbser 1st for loop
            break
    else:
        print num, 'is a prime number'
