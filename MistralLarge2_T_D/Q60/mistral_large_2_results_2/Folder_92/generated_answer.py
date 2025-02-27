from sympy import isprime, primerange

def all_left_right_truncatable_prime(t):
    x = t[7]
    primes = list(primerange(2, x + 1))
    truncatable_primes = []
    for p in primes:
        if '0' in str(p):
            continue
        q = str(p)
        while q:
            if not isprime(int(q)):
                break
            q = q[1:-1]
        else:
            truncatable_primes.append(p)
    return sorted(truncatable_primes)