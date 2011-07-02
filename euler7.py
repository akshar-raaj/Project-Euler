def isPrime(number):
    lowest=2
    highest=number**0.5
    highest=int(highest)
    while(lowest<=highest):
        if(number%lowest==0):
            return False
        lowest=lowest+1
    return True

def generatePrimeNumbers():
    primeCount=0
    numberToBeChecked=1
    requiredPrime=1
    while(primeCount<10001):
        numberToBeChecked=numberToBeChecked+1
        if(isPrime(numberToBeChecked)):
            requiredPrime=numberToBeChecked
            primeCount=primeCount+1
    print ("10001st prime number is {0}".format(requiredPrime))
    
generatePrimeNumbers()
