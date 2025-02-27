def all_right_truncatable_prime(t):
    x = t[32]

    def is_right_truncatable_prime(n):
        if n < 10 and is_prime(n):
            return True
        elif n % 10 == 0:
            return False
        elif is_prime(n):
            return is_right_truncatable_prime(n // 10)
        else:
            return False

    def is_prime(n):
        if n <= 1:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(n ** 0.5) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    return sorted((n for n in range(2, x) if is_right_truncatable_prime(n)))