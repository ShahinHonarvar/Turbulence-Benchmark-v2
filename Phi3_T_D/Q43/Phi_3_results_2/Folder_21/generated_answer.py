from math import sqrt

def find_primes_between_indices(numbers_list):
    prime_numbers = []
    for num in numbers_list[478:950]:
        if num > 1:
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)