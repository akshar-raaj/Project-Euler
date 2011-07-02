#!/usr/bin/python
#filename euler1.py
the_sum=0
for i in range(3,1000):
    if(i%3==0 or i%5==0):
        the_sum+=i
print ("Sum of natural numbers below 1000 which are multiple of either 3 or 5 is is {0}".format(the_sum))
