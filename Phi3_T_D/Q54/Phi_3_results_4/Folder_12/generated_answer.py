def all_right_truncatable_prime(numbers):

    def is_prime(n, cache={2: True}):
        if n < 2:
            return False
        if n not in cache:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            cache[n] = True
        return cache[n]

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[70]
    right_truncatable_primes = [prime for prime in range(2, x) if is_prime(prime) and is_right_truncatable_prime(prime)]
    return sorted(right_truncatable_primes, reverse=True)