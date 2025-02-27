from math import sqrt

def prime_factors(nums):
    num = nums[42]
    for i in range(2, int(sqrt(num)) + 1):
        while num % i == 0:
            num //= i
    return num