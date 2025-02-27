def all_left_right_truncatable_prime(x):
    if len(x) != 1 or x[0] <= 0:
        return []
    x = x[0]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True
    truncatable_primes = [p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes