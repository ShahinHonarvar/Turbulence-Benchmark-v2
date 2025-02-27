from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2 and is_prime(n):
            factors.add(n)
        return factors
    return get_prime_factors(numbers[410])