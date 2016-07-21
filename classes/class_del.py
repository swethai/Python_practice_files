#!/usr/bin/python

#Class definition
#python test.py
class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

#Delete method declaration
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, " destroyed"

#Creation of Point object
pt1 = Point()

#assining reference of pt2 and pt3 to pt1 object
pt2 = pt1
pt3 = pt2

#prints id's of pt1, pt2, pt3
print id(pt1), id(pt2), id(pt3)

#deleting references to object
del pt1
del pt2
del pt3
