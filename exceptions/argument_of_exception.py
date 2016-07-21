#!/usr/bin/python


def var_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "Argument does not contain the number\n", Argument


var_convert('xyz')
