data_file = open('euler13_data')
numbers_sum = sum([int(each_line) for each_line in data_file])
print "First ten digits of the sum of the given one hundred \
50-digits numbers is", str(numbers_sum)[:10]
data_file.close()
