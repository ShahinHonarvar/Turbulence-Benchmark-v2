from math import sqrt

def prime_factors(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors.add(i)
                while n % i == 0:
                    n //= i
        if n > 1 and is_prime(n):
            factors.add(n)
        return factors
    return prime_factors_of(int_list[714])