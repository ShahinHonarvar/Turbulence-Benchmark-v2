from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    primes = {str(p) for p in range(2, x + 1) if isprime(p)}

    def is_truncatable(p, primes_set):
        for i in range(1, len(p)):
            if p[i:] not in primes_set or p[:i] not in primes_set:
                return False
        return True
    for p in primes:
        if len(p) > 1 and is_truncatable(p, primes):
            truncatable_primes.append(int(p))
    return sorted(truncatable_primes)