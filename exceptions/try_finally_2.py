#!/usr/bin/python

#nested try, with finally block can not use except or else block for try
#python test.py

#try block
try:
    fo = open('foo1.txt', 'r')

#Nested try block
    try:
        print "trying to write content to the file"
        fo.write('swetha:writing content to file')
        print "writing content to file clompleted"

#Finally block
    finally:
        print "Closing the file"
        fo.close()
        print "file closed"

#Except block
except IOError:
    print "Can not find a file to write, file opened in read mode"
