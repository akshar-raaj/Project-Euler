#!/usr/bin/python
"""Logic
   The path consists of 20 steps down and 20 steps right.
   So, its is of the form DDDRRR......DDRR.
   Hence it consists of 20 D and 20 R. So, the number of such
   permutations possible is 40!/(20!*20!)"""


def find_factorial(number):
    return reduce(lambda x, y: x * y, range(1, number + 1))

factorial_fourty = find_factorial(40)
factorial_twenty = find_factorial(20)
number_of_paths = factorial_fourty / (factorial_twenty * factorial_twenty)
print "Number of possible routes from top left corner to \
bottom right corner in a 20 by 20 grid is " + str(number_of_paths)
