#!/usr/bin/python
#filename euler2.py



def get_fibonacci_numbers(maxValue):
    # 1, 2, 3, 5, 8
    firstTerm, secondTerm, nextTerm = 1, 2, 0
    yield firstTerm
    yield secondTerm
    while True:
        nextTerm = firstTerm + secondTerm
        firstTerm, secondTerm = secondTerm, nextTerm
        if nextTerm > maxValue:
            break
        yield nextTerm

def sum_fibonacci_upto_this(maxValue):
    the_sum = sum(each for each in get_fibonacci_numbers(maxValue) if each%2 == 0)
    print "Sum is %d" % the_sum

if __name__ == "__main__":
    sum_fibonacci_upto_this(4000000)
