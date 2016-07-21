#!/usr/bin/python


#file operations
#python test.py

#file open, creatinmg file object
fo = open('foo.txt', 'rw+')

#printing file name
print "Name of the file : ", fo.name

#Writing content to file
fo.write("swetha1\nswetha2\nswetha3\nswetha4\nswetha5\n");

#Flushing the content in buffer
fo.flush()

#Returns File Descriptor value
val1 = fo.fileno()
print "file no is: ", val1

#Return if it is connected with interface (if it is a tty)
val2 = fo.isatty()
print "file is atty : ", val2

#file closing the file
fo.close()

#opening afile
fo = open('foo.txt', 'r+')

#reading a line
line1 = fo.readline()
print  line1

#File seeker, changing the position of file seeker
fo.seek(0, 0)

#reading the lines of file
line2 = fo.readlines()
print line2

fo.seek(5, 0)

#tells current position of the file seeker
val3 = fo.tell()
print "current position : ", val3

#returns next line of the file
for index in range(3):
    line = fo.next()
    print "line no %d - %s" %(index,line)

#file seeker
fo.seek(0,2)

#writing fines of code to file
seq = ["swetha4\n", "swetha5\n"]
fo.writelines(seq)

#read line from file
fo.seek(0,0)
line3 = fo.readline()
print "Line before truncate : ", line3

#truncate the file
fo.truncate()

#readline
line4 = fo.readline()
print "Line after truncated: ", line4

fo.close()
