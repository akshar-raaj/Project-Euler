data_file=open("euler13_data")
string_data=data_file.read()
list_of_string_representation_of_number=string_data.split("\n")
del list_of_string_representation_of_number[len(list_of_string_representation_of_number)-1]
numbers_sum=0
for string_rep_each in list_of_string_representation_of_number:
    numbers_sum=numbers_sum+int(string_rep_each)
numbers_sum=str(numbers_sum)
print "First ten digits of the sum of the given one-hundred 50-digit numbers is "+numbers_sum[:10]