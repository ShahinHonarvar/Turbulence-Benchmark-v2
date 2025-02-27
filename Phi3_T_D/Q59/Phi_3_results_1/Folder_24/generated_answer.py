def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[65]
    truncatable_primes = []

    def is_left_truncatable(n):
        if not is_prime(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True
    for prime_candidate in range(2, x):
        if is_left_truncatable(prime_candidate):
            truncatable_primes.append(prime_candidate)
    return sorted(truncatable_primes, reverse=True)