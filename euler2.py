#!/usr/bin/python
#filename euler2.py
def generateFibonacciUptoThis(maxValue):
    firstTerm=1
    secondTerm=2
    nextTerm=0
    sum=secondTerm
    while(True):
        nextTerm=firstTerm+secondTerm
        if(nextTerm>maxValue):
            break
        if(nextTerm%2==0):
            sum+=nextTerm
        firstTerm=secondTerm
        secondTerm=nextTerm
    print ("Sum is {0}".format(sum))
    
generateFibonacciUptoThis(4000000)       
    
