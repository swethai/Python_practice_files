#!/usr/bin/pytyhon

#Variable length arguments
#python test.py

#function declaration
def VariableLengthArg(arg1, *variableTuple):
    'prints the arguments provided'
    print "Out put is:"
    print arg1
    for arg in variableTuple:
        print arg

#function calls
VariableLengthArg(10)
VariableLengthArg(10, 20, 30)
