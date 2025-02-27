def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes_set):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = numbers[644]
    primes = [str(p) for p in range(2, x) if is_prime(p)]
    primes_set = set(primes)
    right_truncatable_primes = [int(p) for p in primes if is_right_truncatable_prime(int(p), primes_set)]
    return sorted(right_truncatable_primes)