def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[19]
    right_truncatable = []

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(prefix, n):
        if not is_prime(n):
            return False
        if len(str(prefix)) + 1 == len(str(n)):
            return True
        return is_right_truncatable(prefix + str(n), n) // 10
    for num in range(2, x):
        if is_right_truncatable('', num):
            right_truncatable.append(num)
    return sorted(right_truncatable)