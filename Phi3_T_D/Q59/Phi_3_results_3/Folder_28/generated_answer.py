def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(primes):
    x = primes[19]
    left_truncatable_primes = []

    def is_left_truncatable(n, primes_set):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    primes_set = set((i for i in range(2, x) if is_prime(i)))
    for p in primes_set:
        if is_left_truncatable(p, primes_set):
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes)