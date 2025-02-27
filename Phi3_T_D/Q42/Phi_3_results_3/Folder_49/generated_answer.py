from math import sqrt

def prime_factors(list_of_integers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, int(sqrt(num)) + 1):
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
        if num > 1 and is_prime(num):
            factors.add(num)
        return factors
    return get_prime_factors(list_of_integers[68])