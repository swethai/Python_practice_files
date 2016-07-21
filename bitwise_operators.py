#!/usr/bin/python

# 60 = 0011 1100
#13 =  0000 1101 

a = 60    
b = 13
c = 0 


c = a & b;
print "a&b", c

c = a | b;
print "a|b", c

c = a ^ b;
print "a^b", c

c = ~a;
print "~a", c

c = a << 2;
print "a<<2", c

c = a >> 2;
print "a>>2", c
