def generate_nth_triangle_number(n):
    n_th_triangle=(n*(n+1))/2
    return n_th_triangle

"""def find_num_of_divisors(number):
    num_of_divisors=2
    start=2
    end=number/2
    end=int(end)
    while(start<=end):
        if(number%start==0):
            num_of_divisors=num_of_divisors+1
        start=start+1
    return num_of_divisors"""

def findDivisors(number):
    start=1
    end=number**0.5
    end=int(end)
    list=[]
    while(start<=end):
        if(number%start==0):
            quotient=number/start
            list.append(start)
            list.append(quotient)
        start=start+1
    return list

is_number_found=False
n=2
triangle_number=1
num_of_divisors=1
while(not is_number_found):
    triangle_number=generate_nth_triangle_number(n)
    #num_of_divisors=find_num_of_divisors(triangle_number)
    list_of_divisors=findDivisors(triangle_number)
    if(len(list_of_divisors)>500):
        break
    n=n+1
print ("Value of the first triangle number to have over five hundred divisors is {0}".format(triangle_number))
#li=findDivisors(28)
#print li
#print generate_nth_triangle_number(10)
#print find_num_of_divisors(28)
    