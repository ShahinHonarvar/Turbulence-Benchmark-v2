def all_right_truncatable_prime(numbers):
    if len(numbers) < 8 or not isinstance(numbers[8], int) or numbers[8] < 2:
        return []

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    up_to = numbers[8]
    right_truncatables = [n for n in range(2, up_to) if is_right_truncatable_prime(n)]
    return sorted(right_truncatables, reverse=True)