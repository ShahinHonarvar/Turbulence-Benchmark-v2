from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums):
    num = nums[1]
    factors = set()
    if is_prime(num):
        factors.add(num)
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
            while num % i == 0:
                num //= i
    if num > 1:
        factors.add(num)
    return factors