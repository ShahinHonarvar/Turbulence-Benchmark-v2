def all_left_truncatable_prime(tup):
    x = tup[429]

    def is_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    truncatable_primes = [p for p in range(x) if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)