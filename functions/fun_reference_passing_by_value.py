#!/usr/bin/python

#call by reference and call by value
#python test.py

#call by reference function declaration
def ChangeValueReference(list):
    'changes the value of argument'

#appending values to list
    list.append([2, 3, 4]);
    print "list in the function", list
    return;

print "call by reference"
list1 = [30, 40, 50]
ChangeValueReference(list1)

print "list out side the function", list1

print "\ncall by value"

#Call by value function declaration
def ChangeValue(list):
    'Changes the value of the argument'

#assigning new values to list
    list = [2,3,4];
    print "list in the function", list
    return;

list = [30, 40, 50]
ChangeValue(list)
print "list outside the loop", list
