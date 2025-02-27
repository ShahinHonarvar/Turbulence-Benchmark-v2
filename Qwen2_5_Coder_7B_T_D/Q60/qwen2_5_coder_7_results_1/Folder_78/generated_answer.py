def all_left_right_truncatable_prime(numbers):
    x = numbers[23]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n //= 10
        return is_prime(n)

    def is_right_truncatable_prime(n):
        while n >= 10:
            if not is_prime(n):
                return False
            n %= 10
        return is_prime(n)

    def is_left_and_right_truncatable_prime(n):
        return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)
    return sorted([n for n in range(2, x + 1) if is_left_and_right_truncatable_prime(n) and '0' not in str(n)])