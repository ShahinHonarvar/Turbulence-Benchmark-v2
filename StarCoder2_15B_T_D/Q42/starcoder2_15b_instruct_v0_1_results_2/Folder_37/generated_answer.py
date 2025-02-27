from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    n = nums[28]
    factors = set()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                factors.add(i)
            if is_prime(n // i):
                factors.add(n // i)
    return factors