def all_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x[3]
    right_truncatable_primes = list(filter(is_prime, range(2, x)))
    return sorted(right_truncatable_primes, reverse=True)