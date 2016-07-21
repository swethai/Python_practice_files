#!/usr/bin/python

#Tuple program
#./test.py

#assiging elements to tuple
tuple1 = ('abcd', 234, 23.4, 'swetha', 345.5)
tuple2 = ('swetha', 234)

#prints complete tuple
print tuple1

#prints first element of the tuple
print tuple1[0]

#prints elements starting from 2nd  to 3rd
print tuple1[1:3]

#prints elements starts from 3rd element
print tuple1[2:]

#prints list two times
print tuple2 * 2

#prints concatinated list
print tuple1 + tuple2
