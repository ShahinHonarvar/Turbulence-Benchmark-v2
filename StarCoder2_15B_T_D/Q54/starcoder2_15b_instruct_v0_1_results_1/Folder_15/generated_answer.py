import itertools
import math
import functools

def all_right_truncatable_prime(args):
    x = args[0]
    combinations = itertools.product(range(2, x + 1), repeat=6)
    primes = filter(math.isprime, combinations)
    right_truncatable_primes = set()
    for prime in primes:
        if functools.reduce(lambda x, y: x * 10 + y, prime) < x:
            right_truncatable_primes.add(prime)
    return sorted(right_truncatable_primes, reverse=True)