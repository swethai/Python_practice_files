#!/usr/bin/python

#Assertion
#python test.py

#function with assertion, assertion will stop the exection of code if assertion false,
#if it is true it will executes code
def kelvinToFahrenheit(temp):
    assert (temp >=0), "Colder than obsolute zero"
    return ((temp-273)*108)+32

#calling function and printing the result
print kelvinToFahrenheit(273)
print int(kelvinToFahrenheit(506.78))
print kelvinToFahrenheit(-1)
