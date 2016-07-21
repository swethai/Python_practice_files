#!/usr/bin/python

#Directories methods
#python test.py

#imporing the os module
import os

#creating the new directory
str = os.mkdir('newdir')
print "new directory created", str

#moving to new directory
str1 = os.chdir('/swetha/Python-script/practice/sample-programs/files/newdir')
print "change directory", str1

#Getting current directory
str3 = os.getcwd()
print "current director", str3

#Creating new directory
os.mkdir('test')

#Deleting the new directory
str4 = os.rmdir('/swetha/Python-script/practice/sample-programs/files/newdir/test')
os.rmdir('/swetha/Python-script/practice/sample-programs/files/newdir')

print "remove dir ", str4
