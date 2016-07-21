#!/usr/bin/python

#data hiding of attribute
#python test.py

#class declaration
class JustCounter:

#attribute declaration for data hiding of attaribute outside the class
    __secretCounter = 0
    print "constructor"

#declaring of count method
    def count (self):
        self.__secretCounter += 1
        print self.__secretCounter

#cteating counter object
counter = JustCounter ()

#calling count method
counter.count()
counter.count()

#trying to access hide attribute of class outside the class
#producess error
#print counter.__secretCounter

#accessing hided attaribute using below expression
print counter._JustCounter__secretCounter
