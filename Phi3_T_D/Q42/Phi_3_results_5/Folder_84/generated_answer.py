from math import sqrt

def prime_factors(integers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    sieve = [True] * (max(integers) + 1)
    p = 2
    while p * p <= max(integers):
        if sieve[p]:
            for i in range(p * p, len(sieve), p):
                sieve[i] = False
        p += 1
    prime_factors = set()
    number_to_factor = integers[685]
    for i in range(2, number_to_factor + 1):
        if sieve[i] and number_to_factor % i == 0:
            prime_factors.add(i)
    return prime_factors