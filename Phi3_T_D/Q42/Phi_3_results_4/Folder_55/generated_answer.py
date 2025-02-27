import math

def prime_factors(nums):

    def prime_factors_number(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    try:
        return prime_factors_number(nums[21])
    except IndexError:
        return set()