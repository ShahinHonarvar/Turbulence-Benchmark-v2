import math

def prime_factors(nums):
    num = nums[851]
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num //= i
    return num