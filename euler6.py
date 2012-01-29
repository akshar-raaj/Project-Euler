#!/usr/bin/python

def sum_of_squares(number):
    """sum=0
    for i in range(1,number+1):
        square=i**2
        sum=sum+square
    return sum"""
    l = [i*i for i in range(1,number+1)]
    return sum(l)

def square_of_sum(number):
    """sum=0
    for i in range(1,number+1):
        sum=sum+i
    return sum**2"""
    l = range(1, number+1)
    return sum(l)**2

sum_of_squre=sum_of_squares(100)
square_of_sum=square_of_sum(100)
print ("Difference between the sum of the squares of the first one hundred "
       "natural numbers and the square of the sum i "
       "{0}".format(square_of_sum-sum_of_squre))
