#!/usr/bin/python

#Overriding operators	
#python test.py

#Class declaration
class Vector:

#constructor declaration
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print"constructor"

#Overloading method declaration, str prints in string repragentation
    def __str__(self):
        print "str"
        return 'Vector (%d, %d")' % (self.a, self.b)
        
#adding 2 vectors, overloading method
    def __add__(self, other):
        print "add"
        return Vector(self.a + other.a, self.b + other.b)

#Objects creation
V1 = Vector(2, 10)
V2 = Vector(5, -2)

#prints id's of class object references
print id(V1)
print id(V2)
print id(V1 + V2)

#prints the string representation result (calls str overloading method)
print V1 + V2

