sum=0
for i in range(1,1001):
    value = pow(i,i)
    sum += value
sum = str(sum)
print "Required number is %s" % sum[len(sum)-10:]