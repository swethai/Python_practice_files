#!/usr/bin/python

#sting methods
#python test.py

str = "this is a string"
#Capitalize(), it capitalizes first character of the string
print "capitalize string : ", str.capitalize()

#center(width[, filler]), it returns centered string with length width. padding is done with mentioned filler.
print "center(width[,filler]) method", str.center(40, 'a')

#str.count(sub, start= 0,end=len(string)), returns no. of occurence of the sub string.
print "str.count(\"i\") : ", str.count("i")
print "str.count(\"string\") : ", str.count("string", 4, 40)


#encoding and decoding of the string
#str.encode(encoding='UTF-8',errors='strict')
#str.encode(encoding='UTF-8',errors='strict')
str1 =  str.encode('base64', 'strict')
print "encoding string : ", str1
print "decoding string : ", str1.decode('base64', 'strict')

#endswith(suffix, beg=0, end=len(string)), returns true if string ends with the specified suffix
print str.endswith('is')
print str.endswith('is', 0,7)

#expandtabs(tabsize), truns copy of the string with tab space expand
str2 = "this is a\tstring"
print "original string : " + str2
print "default expand tab : " + str2.expandtabs()
print "Double expand tabs : " + str2.expandtabs(16)

#str.find(str, beg=0 end=len(string)), return index if found other wise -1
str3 = "this is string example"
print "sub sting find in the string :", str3.find('string')
print "sub string not present in the string : ", str3.find('test')

#index(str, beg=0, end=len(string)), returns true if sub string present in the string, otherwise returns exception
print "index of substring :", str3.index('string')
#print "sub string not present in the string throws exception: ", str3.index('test')

#isalnum() Method, returns true if it is alphanumeric else it returns false for any other characters
str4 = "this2016"
print "string is alphanumeric ", str4.isalnum()
print "string is not alphanumeric ", str3.isalnum()

#isdigit()
print "is digit \'this2016\'", str4.isdigit()
str5 = "123456"
print "is digit \'123456\'", str5.isdigit()

#islower()
str6 = "this is a string"
str7 = "This is a string"
print "is lower \'this is a string\' ", str6.islower()
print "is lower \'This is a string\' ", str7.islower()
