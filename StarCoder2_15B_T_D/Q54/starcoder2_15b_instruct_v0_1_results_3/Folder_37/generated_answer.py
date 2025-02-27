def all_right_truncatable_prime(x):
    x = x[0]

    def is_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        return is_right_truncatable_prime(n // 10)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = [n for n in range(x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes, reverse=True)