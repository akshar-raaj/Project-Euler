#!/usr/bin/python
#filename euler3.py
def isPrime(number):
    sqrtOfNumber=number**0.5
    sqrtOfNumber=int(sqrtOfNumber)
    #print sqrtOfNumber
    for i in range(2,sqrtOfNumber+1):
        if(number%i==0):
            return False
    return True

"""def findPrimeFactors(number):
    maxToCheck=number/2
    maxToCheck=int(maxToCheck)
    isFactorPrime=False
    highestPrimeFactor='a'
    #for i in range(2,maxToCheck+1):
    i=2
    while(i<maxToCheck+1):
        if(number%i==0):
            isFactorPrime=isPrime(i)
            if(isFactorPrime):
                highestPrimeFactor=i
        i=i+1
    print highestPrimeFactor"""
    
def findLowestPrimeNumberBetween(lowerLimit,upperLimit):
    #for i in range(lowerLimit,upperLimit+1):
    i=lowerLimit
    while(i<=upperLimit):
        if(isPrime(i)):
            return i
        i=i+1
    return upperLimit

def factorize(number):
    quotient=number
    lowestPrimeFactor=2
    lowerLimitForPrimeFactorPrimeFactor=lowestPrimeFactor
    primeFactorsList=[]
    while(quotient!=1):
        primeFactor=findLowestPrimeNumberBetween(lowerLimitForPrimeFactorPrimeFactor,quotient)
        if(quotient%primeFactor==0):
            quotient=quotient/primeFactor
            primeFactorsList.append(primeFactor)
            #print primeFactor
        else:
            lowerLimitForPrimeFactorPrimeFactor=lowerLimitForPrimeFactorPrimeFactor+1
    print ("Largest prime factor of {0} is {1}".format(number,primeFactorsList[len(primeFactorsList)-1]))       

factorize(600851475143)
            
