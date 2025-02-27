import math

def prime_factors(num):
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2:
        factors.add(num)
    return factors

def prime_factors_of_15th(nums):
    if len(nums) > 15:
        return prime_factors(nums[15])
    else:
        raise IndexError('List does not contain enough elements.')