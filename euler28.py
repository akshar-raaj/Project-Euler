init_sum =1
current_spiral_numbers_diff = 2
current_number = 3
for i in range(3,1003,2):
    for j in range(1,5):
        init_sum += current_number
        current_number += current_spiral_numbers_diff
    current_spiral_numbers_diff += 2
    current_number = current_number+2
print init_sum
        
    