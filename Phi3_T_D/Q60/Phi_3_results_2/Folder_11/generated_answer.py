def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, original=True):
        if n < 10:
            return True
        if not original and (not is_prime(n)):
            return False
        str_n = str(n)
        if is_prime(int(str_n)):
            return all((is_truncatable_prime(int(str_n[i:]) if original else int(str_n[:i + 1]), False) for i in range(len(str_n))))
        return False
    x = numbers[86] if 0 < 86 < len(numbers) else 0
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)])