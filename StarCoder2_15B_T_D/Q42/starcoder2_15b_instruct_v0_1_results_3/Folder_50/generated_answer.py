import re
import math

def prime_factors(nums):
    num = nums[40]
    prime_factors = []
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            prime_factors.append(i)
            num //= i
    if num > 1:
        prime_factors.append(num)
    return set(prime_factors)