from math import sqrt

def prime_factors(int_list):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            while num % i == 0 and is_prime(i):
                factors.add(i)
                num //= i
        return factors
    return get_prime_factors(int_list[40]) if len(int_list) > 40 else set()