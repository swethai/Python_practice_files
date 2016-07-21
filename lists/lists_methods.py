#!/usr/bin/python

aList = [123, 'swetha', 'xyz', 'abc']
bList = [2009, 'test']
print "aList before append: ", aList  
aList.append(123)

print "aList  after append: ", aList

#count for 123
aList.count(123)

#extending the aList with bList
aList.extend(bList)
print "aList: ", aList

#index of object that the object apears
aList.index('swetha')

#inserting object at offset index
aList.insert(2, 'swetha1')
print "aList: ", aList

#pop the list
aList.pop(2)
print "aList: ", aList

#removing the object from the list
aList.remove('swetha')
print "aList: ", aList

#reversing the list
aList.reverse()

#sorting of the list
aList.sort()
print "Alist: ", aList

