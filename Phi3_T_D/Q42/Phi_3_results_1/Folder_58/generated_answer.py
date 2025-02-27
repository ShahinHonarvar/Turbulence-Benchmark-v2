from math import sqrt

def prime_factors(arr):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        factors = set()
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    if 714 >= len(arr):
        raise IndexError('Index out of range')
    number = arr[714]
    result = prime_factors_of(number)
    return result