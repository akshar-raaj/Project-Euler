dictionary_number_to_word={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred"}
def process_one_digit_number(number):
    word=""
    word=dictionary_number_to_word[number]
    word=word.replace(" ","")
    return word

def process_two_digit_number(number):
    word=""
    string_rep=str(number)
    if(number>=11 and number<=20):
        word= dictionary_number_to_word[number]
    else:
        ones_digit=string_rep[1]
        tens_digit=string_rep[0]
        if(ones_digit!="0"):
            word=dictionary_number_to_word[int(ones_digit)]
            tens_digit=int(tens_digit)
            tens_digit=tens_digit*10
            word=dictionary_number_to_word[tens_digit]+" "+word
        else:
            tens_digit=int(tens_digit)
            tens_digit=tens_digit*10
            word=dictionary_number_to_word[tens_digit]
    word=word.replace(" ","")
    return word
    
def process_three_digit_number(number):
    word=""
    string_rep=str(number)
    if(number%100==0):
        hundreds_digit=string_rep[0]
        word=dictionary_number_to_word[int(hundreds_digit)]+" "+dictionary_number_to_word[100]
    else:
        hundreds_digit=string_rep[0]
        tens_digit=string_rep[1]
        ones_digit=string_rep[2]
        if(tens_digit=="0"):
            word=dictionary_number_to_word[int(hundreds_digit)]+" "+dictionary_number_to_word[100]+" and "
            word=word+dictionary_number_to_word[int(ones_digit)]
        else:
            word=dictionary_number_to_word[int(hundreds_digit)]+" "+dictionary_number_to_word[100]+" and "
            word=word+process_two_digit_number(int(string_rep[1:]))
    word=word.replace(" ","")
    return word

#print process_three_digit_number(115)   

#print process_one_digit_number(8)
   
#print find_corresponding_word_length(9)
word_length_sum=0
for i in range(1,1000):
    if(len(str(i))==1):
        word=process_one_digit_number(i)
    elif(len(str(i))==2):
        word=process_two_digit_number(i)
    else:
        word=process_three_digit_number(i)
    word_length_sum+=len(word)
word_length_sum+=len("onethousand")
print "Letters used to write numbers from 1 to 1000 in words is "+str(word_length_sum)
