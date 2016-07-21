#!/usr/bin/python

#if elif and else condition
#./test.py
#elif condiotions are optional and same as if condition
var1 = 100

#if condition
if var1 == 200:
    print "1- got a true expression"
    print var1

#elif conditions
elif var1 == 150:
    print "2- got a true condition"
    print  var1
elif var1 == 100:
    print "3- got a true condition"
    print var1

#else condition
else:
    print "4- got a false condition"
    print var1

print "good bye!"
