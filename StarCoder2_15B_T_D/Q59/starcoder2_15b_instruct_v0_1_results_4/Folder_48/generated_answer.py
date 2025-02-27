def all_left_truncatable_prime(numbers):
    x = numbers[835]

    def is_left_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0:
            return False
        return is_prime(num) and is_left_truncatable_prime(num // 10)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return sorted([num for num in range(x) if is_left_truncatable_prime(num)])