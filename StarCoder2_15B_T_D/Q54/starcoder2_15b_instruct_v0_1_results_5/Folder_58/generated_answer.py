def all_right_truncatable_prime(ints):
    x = ints[975]

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
    truncatable_primes = []
    for i in range(x):
        n = i
        while n > 0:
            if not is_right_truncatable_prime(n):
                break
            truncatable_primes.append(n)
            n //= 10
    return sorted(truncatable_primes, reverse=True)