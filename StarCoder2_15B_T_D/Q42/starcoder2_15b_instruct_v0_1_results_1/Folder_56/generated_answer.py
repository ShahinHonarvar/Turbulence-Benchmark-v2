import math

def prime_factors(numbers):
    number_at_index_60 = numbers[60]
    prime_factors = set()
    for i in range(2, int(math.sqrt(number_at_index_60)) + 1):
        while number_at_index_60 % i == 0:
            prime_factors.add(i)
            number_at_index_60 /= i
    if number_at_index_60 > 1:
        prime_factors.add(number_at_index_60)
    return prime_factors