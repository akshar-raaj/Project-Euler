#!/usr/bin/python


def is_prime(number):
    start = 2
    end = number ** 0.5
    end = int(end)
    while start <= end:
        if(number % start == 0):
            #print start
            return False
        start = start + 1
    #print number
    return True


def sum_primes_below(number):
    i = 3  # We start testing prime numbers starting from 3
    primes_sum = 2
    while(i <= number):
        if(is_prime(i)):
            primes_sum = primes_sum + i
	"We know that an even number cannot \
	be prime. So, we increase it in steps of 2"
	i = i + 2
    print ("Sum of all the primes below two million is " + str(primes_sum))

sum_primes_below(2000000)
