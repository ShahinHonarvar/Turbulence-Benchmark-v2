def all_right_truncatable_prime(numbers):
    x = numbers[618]

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, x):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    return sorted([i for i in range(2, x) if is_right_truncatable_prime(i, x) and is_prime(i)])