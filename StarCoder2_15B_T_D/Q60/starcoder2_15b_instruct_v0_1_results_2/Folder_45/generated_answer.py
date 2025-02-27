def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if not is_prime(n):
            return False
        if len(s) <= 2:
            return True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    x = x[61]
    return sorted((n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)))