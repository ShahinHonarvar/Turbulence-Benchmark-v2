import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime

def is_left_truncatable_prime(n, prime):
    while n > 0:
        if not prime[n]:
            return False
        n //= 10
    return True

def all_left_truncatable_prime(tup):
    x = tup[645]
    prime = sieve_of_eratosthenes(x)
    result = []
    for i in range(2, x):
        if prime[i] and is_left_truncatable_prime(i, prime):
            result.append(i)
    return sorted(result)