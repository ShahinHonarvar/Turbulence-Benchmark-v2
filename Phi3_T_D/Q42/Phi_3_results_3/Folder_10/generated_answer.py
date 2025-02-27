import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    n = lst[54]
    factors = set()
    for i in range(2, n + 1):
        if is_prime(i) and n % i == 0:
            factors.add(i)
    return factors