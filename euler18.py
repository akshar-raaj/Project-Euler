class NumberAlongWithMaximumTillHere:
    def __init__(self,number,maximum):
        self.number=number
        self.maximum=maximum
        
    def set_maximum(self,maximum):
        self.maximum=maximum
        
    def get_number(self):
        return self.number
    
    def get_maximum(self):
        return self.maximum
    
f=open("euler18_data")
file_content=f.read()
li=file_content.split("\n")
del li[len(li)-1]
list_containing_rows=[]
for each in li:
    temp_string_list=each.split(" ")
    temp_int_list=[]
    for e in temp_string_list:
        e=int(e)
        num_along_with_max=NumberAlongWithMaximumTillHere(e,0)
        temp_int_list.append(num_along_with_max)
    list_containing_rows.append(temp_int_list)
first_row_first_number=list_containing_rows[0][0]
first_row_first_number.set_maximum(first_row_first_number.get_number())
for i in range(1, len(list_containing_rows)):
    current_row=list_containing_rows[i]
    previous_row=list_containing_rows[i-1]
    current_row[0].set_maximum(previous_row[0].get_maximum()+current_row[0].get_number())
    for j in range(1,len(current_row)-1):
        if(previous_row[j-1].get_maximum()>previous_row[j].get_maximum()):
            current_row[j].set_maximum(previous_row[j-1].get_maximum()+current_row[j].get_number())
        else:
            current_row[j].set_maximum(previous_row[j].get_maximum()+current_row[j].get_number())
    length_current_row=len(current_row)
    current_row[length_current_row-1].set_maximum(previous_row[length_current_row-2].get_maximum()+current_row[length_current_row-1].get_number())
      
last_row=list_containing_rows[len(list_containing_rows)-1]
li=[]
for each in last_row:
    li.append(each.get_maximum())
li.sort()
print "Maximum total from top to bottom of given triangle is", li[len(li)-1]
    
        
#print list_containing_rows