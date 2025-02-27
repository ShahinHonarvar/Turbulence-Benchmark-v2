import math

def prime_factors(nums):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    factors = set()
    num = nums[8]
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2 and is_prime(num):
        factors.add(num)
    return factors