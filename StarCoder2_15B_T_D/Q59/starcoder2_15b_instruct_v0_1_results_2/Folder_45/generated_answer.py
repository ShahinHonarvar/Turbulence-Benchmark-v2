def all_left_truncatable_prime(numbers):
    x = numbers[61]

    def is_truncatable_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_truncatable_prime, range(2, x)))