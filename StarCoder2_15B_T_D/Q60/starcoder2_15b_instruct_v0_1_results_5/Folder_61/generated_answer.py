def all_left_right_truncatable_prime(x):
    x = x[3]

    def is_prime(n):
        if n in [2, 3]:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable(n)], reverse=True)