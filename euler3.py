#!/usr/bin/python
#filename euler3.py
def isPrime(number):
    sqrtOfNumber = int(number**0.5)
    return all(bool(number % i) for i in xrange(2, sqrtOfNumber + 1))

def findLowestPrimeNumberBetween(lowerLimit,upperLimit):
    return next((i for i in xrange(lowerLimit, upperLimit) if isPrime(i)), upperLimit)

def factorize(number):
    quotient=number
    lowerLimitForPrimeFactor=2
    while(quotient!=1):
        primeFactor=findLowestPrimeNumberBetween(lowerLimitForPrimeFactor,quotient)
        if(quotient%primeFactor==0):
            quotient=quotient/primeFactor
        else:
            lowerLimitForPrimeFactor=lowerLimitForPrimeFactor+1
    print ("Largest prime factor of {0} is {1}".format(number,primeFactor))       

factorize(600851475143)

#print isPrime(4)
#print isPrime(8)
#print isPrime(11)
#print isPrime(12)
#print isPrime(13)
#print isPrime(14)
#print isPrime(51)
#print isPrime(53)
#print isPrime(4)

            
