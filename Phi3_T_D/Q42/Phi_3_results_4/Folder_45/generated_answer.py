from math import sqrt

def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
                while num % i == 0:
                    num //= i
        if num > 1 and is_prime(num):
            factors.add(num)
        return factors
    return get_prime_factors(numbers[33])