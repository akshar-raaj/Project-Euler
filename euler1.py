#!/usr/bin/python -tt
the_sum = sum(num for num in xrange(3, 1000) if num % 3 == 0 or num % 5 == 0)
print """Sum of natural numbers below 1000 which are multiple \
of either 3 or 5 is is %d""" % (the_sum,)
