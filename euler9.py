limit=1000
def is_pythagorean_triplet(a,b,c):
    if(a**2+b**2==c**2):
        return True
    return False

def is_sum_thousand(a,b,c):
    if(a+b+c==1000):
        return True
    return False

def find_required_pythagorean_triplet():
    requiredNumber=0
    for a in range(1,1000):
        for b in range(a+1,1000):
            for c in range(b+1,1000):
                if(is_pythagorean_triplet(a,b,c) and is_sum_thousand(a,b,c)):
                #if((a**2+b**2==c**2) and (a+b+c==1000)):
                    requiredNumber=a*b*c
                    print ("Product abc for only pythagorean triplet for which a+b+c is 1000 is {0}".format(requiredNumber))
                    return
                
find_required_pythagorean_triplet()
#print is_pythagorean_triplet(3,4,7)
#print is_sum_thousand(100,200,600)