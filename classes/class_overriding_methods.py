#!/usr/bin/python

#overriding Parent method in child
#if need any special or different functionality in the child class
#python test.py

#Parent class declaration
class Parent:

#method declaration the Patent
    def myMethod(self):
        print "calling parent method"

#Child class declaration
class child(Parent):

#method declaration in the child for overridding
    def myMethod(self):
        print "Calling Child method"

#instance of child
c = child()

#child calls overridden method
c.myMethod()    
