#!/usr/bin python

#class declaratoion and object creation for the class 
#and accessing of the attributes
#python test.py

#python call Employee
class Employee:
    'Commnbase class for all employees'
    empCount = 0

#Class constructor or initialization method, 
#python call when creating new instance of class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

#Defining function to display emp count
    def displayCount(self):
        print "total employees %d" % Employee.empCount
   
#Defing function to display employee details
    def displayEmployee(self):
        print "Name : ", self.name, ", salary : ", self.salary

#Creating object for the class Employee
emp1 = Employee('test1', 20000)
#emp1.age = 7

#Creating seccond object for the class Employee
emp2 = Employee('test2', 30000)

#Accessing attributes to display employee details	
emp1.displayEmployee()
emp2.displayEmployee()

print "Total employee %d" % Employee.empCount

#function to access the class attributes
print hasattr(emp1, 'age')
 
print getattr(emp1, 'salary')
print setattr(emp1, 'salary', 50000)

print setattr(emp1, 'age', 20)
emp1.displayEmployee()
print delattr(emp1, 'age')

emp1.displayEmployee()
