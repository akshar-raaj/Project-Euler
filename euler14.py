def generate_collatz_sequence(number):
    chain_length = 0
    start = number
    while start != 1:
        chain_length = chain_length + 1
        start = start / 2 if start % 2 == 0 else 3 * start + 1
    chain_length += 1
    return chain_length

start_number = 1
highest_chain_length = 0
number_with_highest_chain_length = 0
while start_number <= 1000000:
    chain_length_current = generate_collatz_sequence(start_number)
    if highest_chain_length < chain_length_current:
        highest_chain_length = chain_length_current
        number_with_highest_chain_length = start_number
    start_number += 1
print "The starting number under 1 million that produces the longest \
chain is " + str(number_with_highest_chain_length)
