def all_right_truncatable_prime(t):
    x = t[992]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True
    right_truncatable_primes = [i for i in range(2, x) if right_truncatable(i)]
    return right_truncatable_primes