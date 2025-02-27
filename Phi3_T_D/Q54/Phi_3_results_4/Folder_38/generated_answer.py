def all_right_truncatable_prime(numbers):
    x = numbers[28]
    right_truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, x):
        return is_prime(n) and all((is_prime(n // 10 ** i) for i in range(len(str(n))) if n // 10 ** i != 0))
    for n in range(2, x):
        if is_right_truncatable(n, x):
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes)