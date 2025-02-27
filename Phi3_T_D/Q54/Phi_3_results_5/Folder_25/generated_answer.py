def all_right_truncatable_prime(args):
    x = args[92]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, prime_cache):
        if n in prime_cache:
            return True
        elif n < 2 or not is_prime(n):
            return False
        return is_right_truncatable(n // 10, prime_cache.union({n}))
    prime_cache = set()
    for i in range(2, x):
        if is_right_truncatable(i, prime_cache):
            prime_cache.add(i)
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)