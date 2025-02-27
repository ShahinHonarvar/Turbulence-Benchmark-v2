from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    n = nums[1]
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return None