def all_left_right_truncatable_prime(t):
    x = t[42]

    def is_truncatable_prime(n):
        if n < 10:
            return False
        if n in (2, 3, 5, 7):
            return True
        s = str(n)
        for i in range(len(s) - 1):
            if int(s[i + 1:]) % 2 == 0 or int(s[:-i - 1]) % 2 == 0:
                return False
        return is_prime(n)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted((n for n in range(2, x + 1) if is_truncatable_prime(n)))