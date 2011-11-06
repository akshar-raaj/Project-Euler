init_sum =1
current_spiral_numbers_diff = 2 #For the 3 by 3 spiral, difference between diagonal elements is 3
current_number = 3
for i in range(3,1003,2): #Next to 3 by 3 spiral, its 5 by 5 spiral followed by 7 by 7 and so on till 1001 by 1001 
    for j in range(1,5): #Four elements in each spiral needs to be considered except "1" which is alreadey taken into account in init_sum
        init_sum += current_number
        current_number += current_spiral_numbers_diff
    current_spiral_numbers_diff += 2 #For each spiral, difference between diagonal keeps increasing by 2, i.e for 3 by 3 spiral its 2, for 5 by 5 spiral its 4 and so on.
    current_number = current_number+2
print init_sum
        
    