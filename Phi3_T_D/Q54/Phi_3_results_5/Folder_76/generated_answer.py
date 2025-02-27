def test_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def all_right_truncatable_prime(t):
    x = t[370]
    primes = [str(p) for p in range(2, x) if test_prime(p)]
    right_truncatable_primes = []
    for prime in primes:
        while prime != '':
            if not test_prime(int(prime)):
                break
            right_truncatable_primes.append(int(prime))
            prime = prime[:-1]
    return sorted(right_truncatable_primes, reverse=True)