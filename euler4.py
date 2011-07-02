#!/usr/bin/python

def isPalindrome(number):
    stringRepresentationOfNumber=str(number)
    if stringRepresentationOfNumber == stringRepresentationOfNumber[::-1]:
        return True
    return False

def findHighestPalindrome():
    highestPalindrome=1
    for i in range(100,1000):
        for j in range(100,1000):
            product=i*j
            if(isPalindrome(product) and product>highestPalindrome):
                highestPalindrome=product
    print ("Largest palindrome made from the product of two 3-digit numbers is {0}".format(highestPalindrome))

findHighestPalindrome()
