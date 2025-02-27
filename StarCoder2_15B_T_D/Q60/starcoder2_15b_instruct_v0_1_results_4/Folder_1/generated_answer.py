def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or not is_prime(n):
            return False
        return is_truncatable_prime(n // 10)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[20]
    truncatable_primes = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)