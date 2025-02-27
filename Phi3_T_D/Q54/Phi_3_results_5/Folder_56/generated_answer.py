def all_right_truncatable_prime(seq):
    primes = (2, 3, 5, 7)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, primedigits):
        if n == 0:
            return True
        if not is_prime(n) or n not in primedigits:
            return False
        return is_right_truncatable(n // 10, primedigits)
    x = seq[30]
    trunc_primes = [p for p in primes if p < x]
    primedigits = set((p for p in primes if p < x))
    while trunc_primes and trunc_primes[-1] // 10 > 0:
        next_primes = [p for p in primedigits if p > 10 and is_right_truncatable(p // 10, primedigits)]
        trunc_primes.extend(next_primes)
        primedigits.update(next_primes)
    return sorted(set(trunc_primes))