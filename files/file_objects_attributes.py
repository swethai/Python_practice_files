#!/usr/bin/python

#File object Arrributes
#python test.py

#opening a file
fo = open("foo.txt", "wb")

#prints name of the file
print "name of the file :", fo.name

#prints access mode of the file
print "access mode of the file:", fo.mode

#prints true/false for the file close
print "closed or not:", fo.closed

#prints true/false, returens false if space explicitly required with print
print "softspace :", fo.softspace


