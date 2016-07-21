#!/usr/bin/python

#Built in class attributes
#python test.py

#Class delaration
class Employee: 
    'commom base class for Employee'
    
    empCount = 0

#function to construct the class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
#Definin the employee count function
    def displayCount():
        print "total count %d" % Employee.empCount
        
#Function definition to display employee details
    def displayEmployee(self):
        print "name : ", self.name, " , salary : ", self.salary

#cteation of Employee object
emp1 = Employee('swetha', 20)

#calling displayEmployee function to display employee details
emp1.displayEmployee()

#Built in attributes
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases_
print "Employee.__dict__:", Employee.__dict__


    
