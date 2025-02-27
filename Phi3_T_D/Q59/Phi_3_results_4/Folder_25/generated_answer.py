def is_prime(n, sieve=None):
    if n <= 1:
        return False
    if sieve is None:
        sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve[n]

def is_left_truncatable_prime(n, sieve=None):
    if n < 10:
        return is_prime(n, sieve)
    return is_prime(n, sieve) and all((is_prime(int(n[i:]), sieve) for i in range(1, len(str(n)))))

def all_left_truncatable_primes(tup):
    x = tup[92]
    sieve = [True] * x
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = [False] * len(range(i * i, x, i))
    return sorted(set((n for n in range(2, x) if is_left_truncatable_prime(n, sieve))))