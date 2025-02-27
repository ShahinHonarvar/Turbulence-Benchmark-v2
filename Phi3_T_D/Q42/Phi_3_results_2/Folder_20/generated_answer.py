from math import sqrt

def prime_factors(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        for i in range(2, int(sqrt(n)) + 1):
            while n % i == 0:
                if is_prime(i):
                    factors.add(i)
                n //= i
        if is_prime(n):
            factors.add(n)
        return factors
    return get_prime_factors(nums[53])