import math

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def is_left_truncatable_prime(n, is_prime):
    if n < 10:
        return is_prime[n]
    return is_prime[n] and is_left_truncatable_prime(n % 10 ** int(math.log10(n)), is_prime)

def all_left_truncatable_prime(tup):
    x = tup[39]
    is_prime = sieve_of_eratosthenes(x)
    return sorted([i for i in range(x) if is_left_truncatable_prime(i, is_prime)])