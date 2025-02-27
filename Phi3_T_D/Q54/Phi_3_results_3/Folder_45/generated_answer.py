def all_right_truncatable_prime(t):
    x = t[61]
    right_truncatable_primes = []
    primes_set = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n = n // 10
            if n > 0 and (not is_prime(n)):
                return False
        return True
    for potential_prime in range(2, x):
        if is_prime(potential_prime):
            if is_right_truncatable_prime(potential_prime):
                right_truncatable_primes.append(potential_prime)
                primes_set.add(potential_prime)
    return sorted(right_truncatable_primes)