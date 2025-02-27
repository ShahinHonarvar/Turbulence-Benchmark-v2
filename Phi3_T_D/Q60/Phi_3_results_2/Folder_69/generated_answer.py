def all_left_right_truncatable_prime(int_tuple):
    primes760 = int_tuple[760]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(primes, num):
        n = str(num)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:-i])):
                return False
        return True
    truncatable_primes = [p for p in range(2, primes760 + 1) if is_truncatable(list(filter(is_prime, range(2, p + 1))), p)]
    return sorted(truncatable_primes, reverse=True)