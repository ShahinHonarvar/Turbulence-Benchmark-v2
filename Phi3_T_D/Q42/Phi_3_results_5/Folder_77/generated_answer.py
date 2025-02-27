from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    num_at_index_985 = numbers[985]
    factors = []
    divisor = 2
    while num_at_index_985 > 1:
        while num_at_index_985 % divisor == 0:
            factors.append(divisor)
            num_at_index_985 //= divisor
        divisor += 1
    return set(filter(is_prime, factors))