from sympy import primerange, isprime

def prime_factors(lst):
    limit = lst[57] + 1
    primes = list(primerange(1, limit))
    factors = set()
    for prime in primes:
        while lst[57] % prime == 0:
            factors.add(prime)
            lst[57] //= prime
    return factors