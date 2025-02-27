def all_left_truncatable_prime(t):
    x = t[29]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        if not is_prime(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = n % 10 ** (len(str(n)) - 1)
        return True
    return sorted([n for n in range(3, x) if left_truncatable(n)], reverse=True)