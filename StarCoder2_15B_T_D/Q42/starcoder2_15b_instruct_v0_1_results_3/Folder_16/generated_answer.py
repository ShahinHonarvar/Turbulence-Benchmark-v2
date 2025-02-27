import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    number_at_index_162 = numbers[162]
    prime_factors_set = set()
    for i in range(2, number_at_index_162 + 1):
        if number_at_index_162 % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set