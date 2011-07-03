#!/usr/bin/python

def isPrime(number):
    start=2
    end=number**0.5
    end=int(end)
    while(start<=end):
        if(number%start==0):
            #print start
            return False
        start=start+1
    #print number
    return True

def sum_primes_below(number):
    i=3 #We start testing prime numbers starting from 3
    sum=2 #Since we did not test 2, we have included it in the sum
    while(i<=number):
        if(isPrime(i)):
            sum=sum+i
        i=i+2 #We know that an even number cannot be prime. So, we increase it in steps of 2
    print ("Sum of all the primes below two million is "+str(sum))

sum_primes_below(2000000)