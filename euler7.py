def is_prime(number):
    lowest = 2
    highest = number ** 0.5
    highest = int(highest)
    while lowest <= highest:
        if number % lowest == 0:
            return False
        lowest = lowest + 1
    return True


def generate_prime_numbers():
    primeCount = 0
    numberToBeChecked = 1
    requiredPrime = 1
    while primeCount < 10001:
        numberToBeChecked = numberToBeChecked + 1
        if is_prime(numberToBeChecked):
            requiredPrime = numberToBeChecked
            primeCount = primeCount + 1
    print ("10001st prime number is {0}".format(requiredPrime))

if __name__ == "__main__":
    generate_prime_numbers()
