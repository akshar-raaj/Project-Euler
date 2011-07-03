product=1
for i in range(1,101):
    product*=i
#print product
product=str(product)
digits_sum=0
for each in product:
    digits_sum+=int(each)
print "Sum of digits in 100! is "+str(digits_sum)