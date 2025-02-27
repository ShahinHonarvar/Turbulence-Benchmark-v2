import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(nums):
    if len(nums) <= 59:
        return []
    n = nums[59]
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                factors.add(i)
            n //= i
            while n % i == 0 and is_prime(i):
                n //= i
    if n > 1:
        factors.add(n)
    return factors