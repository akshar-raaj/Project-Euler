product = reduce(lambda x, y: x * y, range(1, 101))
digits_sum = sum([int(each) for each in str(product)])
print "Sum of digits in 100! is", digits_sum
