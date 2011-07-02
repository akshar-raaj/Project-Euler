#!/usr/bin/python
#filename euler6.py
def sumOfSquares(number):
    sum=0
    for i in range(1,number+1):
        square=i**2
        sum=sum+square
    return sum

def squareOfSum(number):
    sum=0
    for i in range(1,number+1):
        sum=sum+i
    return sum**2

sumOfSqure=sumOfSquares(100)
squareOfSum=squareOfSum(100)
print ("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {0}".format(squareOfSum-sumOfSqure))
