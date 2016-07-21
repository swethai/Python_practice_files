#!/usr/bin/python

#Default Arguments function declaration
#python test.py

#function declaration
def DefaultArguments(name = 'test', age = 20):
    'prints name and age'
    print "name : %s, age : %d" %(name, age)
    
#function calls
DefaultArguments(name='swetha', age=25)
DefaultArguments(name='swetha1')
