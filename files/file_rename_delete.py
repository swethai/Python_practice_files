#!/usr/bin/python

#Renaming and deletin the files
#python test.py

#imporing the os module
import os 

#Renaming the file
os.rename('foo1.txt', 'foo.txt')
fo = open('foo.txt', 'r+')
str1 = fo.read(10);
print str1

#Removing the file
os.remove('foo.txt')
