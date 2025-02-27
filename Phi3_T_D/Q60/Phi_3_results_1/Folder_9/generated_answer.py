def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_and_right_truncatable(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        if len(str_n) == 1:
            return True
        return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(1, len(str_n))))
    x = numbers[29] if 29 < len(numbers) else None
    if x is None:
        return []
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable(i)], reverse=True)