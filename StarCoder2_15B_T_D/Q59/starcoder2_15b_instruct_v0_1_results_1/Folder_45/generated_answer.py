def all_left_truncatable_prime(tup):
    x = tup[61]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num >= 10:
            num //= 10
            if not is_prime(num):
                return False
        return True
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes)