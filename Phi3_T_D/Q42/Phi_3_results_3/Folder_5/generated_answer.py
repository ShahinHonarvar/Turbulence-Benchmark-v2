from math import sqrt

def prime_factors(integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        return set((factor for i in range(2, n + 1) if n % i == 0 and is_prime(i)))
    if len(integers) < 68:
        raise IndexError('List does not have enough elements')
    return factors(integers[67])