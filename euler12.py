generate_nth_triangle_number = lambda x: (x * (x + 1)) / 2


def findDivisors(number):
    end = int(number ** 0.5)
    number_of_divisors = 0
    for i in xrange(1, end + 1):
        if number % i == 0:
            number_of_divisors += 2
    return number_of_divisors

from itertools import count
for i in count(2):
    triangle_number = generate_nth_triangle_number(i)
    num_of_divisors = findDivisors(triangle_number)
    if num_of_divisors > 500:
        break

print ("First triangle number to have over\
 five hundred divisors is {0}".format(triangle_number))
