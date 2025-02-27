def all_right_truncatable_prime(numbers):
    x = numbers[39]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if n == 0:
            return True
        if not is_prime(n) or n not in primes:
            return False
        return is_right_truncatable_prime(n // 10, primes)
    primes = [i for i in range(2, x) if is_prime(i)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes)]
    return sorted(right_truncatable_primes, reverse=True)