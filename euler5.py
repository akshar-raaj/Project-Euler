#!/usr/bin/python
#filename euler5.py
def findLCMofNumbersUptoThis():
    step=0
    shouldContinue=True
    while(shouldContinue):
        step=step+20
        if(step%11==0 and step%12==0 and step%13==0 and step%14==0 and step%15==0 and step%16==0 and step%17==0 and step%18==0 and step%19==0 and step%20==0):
            shouldContinue=False
    print ("Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {0}".format(step))
findLCMofNumbersUptoThis()
                
            
