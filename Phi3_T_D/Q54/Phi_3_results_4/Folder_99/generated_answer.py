def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes_set):
        if n < 10:
            return False
        while n > 0:
            if not is_prime(n):
                return False
            primes_set.add(n)
            n = n // 10
        return True
    primes_set = set()
    trunc_primes = []
    prime_range = range(2, num_tuple[758])
    for p in prime_range:
        if is_right_truncatable_prime(p, primes_set):
            trunc_primes.append(p)
    return sorted(trunc_primes)