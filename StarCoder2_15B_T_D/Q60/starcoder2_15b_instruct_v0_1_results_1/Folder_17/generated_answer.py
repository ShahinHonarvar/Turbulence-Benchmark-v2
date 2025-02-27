def all_left_right_truncatable_prime(numbers):
    x = numbers[36]

    def is_truncatable_prime(num):
        if num < 10:
            return num in (2, 3, 5, 7)
        return num in (2, 3, 5, 7) and is_truncatable_prime(num // 10) and is_truncatable_prime(num % 100)
    return sorted(filter(is_truncatable_prime, range(1, x + 1)), reverse=True)