#!/usr/bin/python


#File positions
#python test.py

#open a file
fo = open("foo.txt", "r+")

#Reading a file content of 10 bytes
str1 = fo.read(10);
print "read string is ", str1

#chek current position
position = fo.tell();
print "Current position is ", position

#Read file content from current position
str2 = fo.read(10);
print "reading string after position is ", str2

#Repositioning the pointer at the beginning of the file
position = fo.seek(0, 0);

#Reading the file seeking the position
str = fo.read(10)
print "read string is after seeking the position to begin", str

#closing the file
fo.close()
