from functools import reduce
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) <= 46:
        return set()
    number_at_46 = numbers[46]
    factors = set()
    for i in range(2, number_at_46 + 1):
        if number_at_46 % i == 0:
            if is_prime(i):
                factors.add(i)
    return factors