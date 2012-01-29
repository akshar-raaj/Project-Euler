#!/usr/bin/python

def isPalindrome(number):
    """stringRepresentationOfNumber=str(number)
    if stringRepresentationOfNumber == stringRepresentationOfNumber[::-1]:
        return True
    return False"""
    return str(number) == str(number)[::-1]

def findHighestPalindrome():
    """highestPalindrome=1
    for i in range(100,1000):
        for j in range(100,1000):
            product=i*j
            if(isPalindrome(product) and product>highestPalindrome):
                highestPalindrome=product"""
    numbers = [i*j for i in range(100,1000) for j in range(100,1000) if isPalindrome(i*j)]
    highestPalindrome = max(numbers)
    print "Largest palindrome made from the product of two 3-digit numbers is %d" % (highestPalindrome,)

findHighestPalindrome()
