import sympy

def all_left_truncatable_prime(tup):
    x = tup[69]
    primes = [p for p in sympy.primerange(2, x) if '0' not in str(p)]
    left_truncatable_primes = []
    for prime in primes:
        p = prime
        while p > 0:
            if not sympy.isprime(p):
                break
            p = int(str(p)[1:])
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)