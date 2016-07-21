#!/usr/bin/python

#Parent Class declaration
#python test.py
class Parent:
    parentAttr = 100

#Parent class constructor declaration
    def __init__(self):
        print "Calling Parent constructor"

#Parent class method declaration
    def parentMethod(self):
        print "Calling Parent Method"

#Parent class setAttr method declaration
    def setAttr(self, attr):
        Parent.parentAttr = attr
        print "setattr"
 
#Parent getAttr method declaration
    def getAttr(self):
        print "Parent Attribute", Parent.parentAttr


#Child class declaration
class  Child(Parent):
    
#Child class constructor declaration
    def __init__(self):
        print "Calling Child Constructor"

#Child class method declaration
    def childMethod(self):
        print "Calling child method"

#Child class object creation
c = Child()

#callimg child class method
c.childMethod()

#Calling Parent class method
c.parentMethod()

#Calling Parent setAttr method
c.setAttr(200)

#Calling Parent getAttr method
c.getAttr()
