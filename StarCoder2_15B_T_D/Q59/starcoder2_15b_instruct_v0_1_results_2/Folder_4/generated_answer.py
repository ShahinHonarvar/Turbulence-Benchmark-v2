def all_left_truncatable_prime(t):
    x = t[96]

    def is_left_truncatable_prime(n):
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
    return sorted((n for n in range(2, x) if is_left_truncatable_prime(n)), reverse=True)