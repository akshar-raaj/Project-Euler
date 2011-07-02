#!/usr/bin/python
#filename euler4.py

def isPalindrome(number):
    stringRepresentationOfNumber=str(number)
    #print stringRepresentationOfNumber
    length=len(stringRepresentationOfNumber)
    for i in range(0,length/2):
        if(stringRepresentationOfNumber[i]!=stringRepresentationOfNumber[length-1-i]):
            return False
    return True

def findHighestPalindrome():
    highestPalindrome=1
    for i in range(100,1000):
        for j in range(100,1000):
            product=i*j
            if(isPalindrome(product) and product>highestPalindrome):
                highestPalindrome=product
    print ("Largest palindrome made from the product of two 3-digit numbers is {0}".format(highestPalindrome))

findHighestPalindrome()
