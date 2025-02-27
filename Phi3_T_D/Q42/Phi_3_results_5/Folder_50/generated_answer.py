import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    if len(nums) < 41:
        return set()
    number = nums[40]
    factors = set()
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    return factors