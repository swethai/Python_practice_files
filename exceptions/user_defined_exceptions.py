#!/usr/bin/python

#User defined exception
#python test.py

#Class defination for subclass of RuntimeError
class NWerror(RuntimeError):
    def __init__(self, arg):
        self.arg = arg

#try block rises exception
try:
    raise NWerror("bad host")

#Excep block prints argments of class
except NWerror,e:
    print e.arg
