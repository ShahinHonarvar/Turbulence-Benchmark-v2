from typing import Tuple
import sympy

def all_left_truncatable_prime(tup: Tuple[int]) -> list:
    x = tup[70]
    primes = sympy.primerange(2, x)
    left_truncatable = [p for p in primes if all((sympy.isprime(int(str(p)[i:])) for i in range(len(str(p)))))]
    return sorted(left_truncatable, reverse=True)