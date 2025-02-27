def all_right_truncatable_prime(t):
    x = t[71]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = [p for p in range(2, x) if is_right_truncatable_prime(p)]
    return sorted(right_truncatable_primes, reverse=True)