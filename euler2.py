#!/usr/bin/python
#filename euler2.py
def sum_fibonacci_upto_this(maxValue):
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
    
if __name__=="__main__":
    sum_fibonacci_upto_this(4000000)       
    
