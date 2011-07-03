def generate_collatz_sequence(number):
    chainLength=0
    start=number
    while(start!=1):
        chainLength+=1
        if(start%2==0):
            start=start/2
        else:
            start=3*start+1
    chainLength+=1
    return {number:chainLength}

#generate_collatz_sequence(13)
#li=dict.keys()
#value=dict[li[0]]
#print li, value
start_number=1
highest_chain_length=0
number_with_highest_chain_length=0
while(start_number<=1000000):
    dictionary_current=generate_collatz_sequence(start_number)
    #print dictionary_current,
    key_list_current=dictionary_current.keys()
    #print key_list_current,
    chain_length_current=dictionary_current[key_list_current[0]]
    #print chain_length_current
    if(highest_chain_length<chain_length_current):
        highest_chain_length=chain_length_current
        number_with_highest_chain_length=key_list_current[0]
    start_number+=1
print "The starting number under 1 million that produces the longest chain is "+str(number_with_highest_chain_length)
    