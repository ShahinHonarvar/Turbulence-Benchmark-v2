def all_right_truncatable_prime(numbers):
    if len(numbers) < 25 or not isinstance(numbers[24], int):
        raise ValueError('The tuple must contain at least 25 elements with the integer at index 24.')
    x = numbers[24]
    primes = [2, 3, 5, 7]

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def trim_last_digit(n):
        return n // 10 if n > 9 else 0

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = trim_last_digit(n)
        return True
    right_truncatable_primes = [p for p in range(7, x) if is_right_truncatable(p)]
    return sorted(right_truncatable_primes, reverse=True)