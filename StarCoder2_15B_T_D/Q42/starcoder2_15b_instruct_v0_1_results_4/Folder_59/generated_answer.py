import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    n = nums[2]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return set(prime_factors(n // i) + prime_factors(i))
    return [n] if is_prime(n) else []