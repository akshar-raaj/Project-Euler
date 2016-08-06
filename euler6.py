#!/usr/bin/python


def sum_of_squares(number):
    l = (i * i for i in xrange(1, number + 1))
    return sum(l)


def square_of_sum(number):
    l = xrange(1, number + 1)
    return sum(l) ** 2

sum_of_squre = sum_of_squares(100)
square_of_sum = square_of_sum(100)
print ("Difference between the sum of the squares of the first one hundred "
       "natural numbers and the square of the sum is "
       "{0}".format(square_of_sum - sum_of_squre))
