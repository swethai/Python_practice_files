#!/usr/bin/python

#file write and read operations
#python test.py

#file open
fo = open("foo.txt", "r+")
print "Name of the file", fo.name

#writing content to file
fo.write( "python is great language. \nYeah its great!!\n");

#closing the file
fo.close()

#opening the file
fo = open("foo.txt", "r+");

#reading the file
str1 = fo.read(10);

#printing the read content
print str1

#closing the file
fo.close()
