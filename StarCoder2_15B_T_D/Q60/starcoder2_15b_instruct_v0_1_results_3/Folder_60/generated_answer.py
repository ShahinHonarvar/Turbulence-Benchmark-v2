def all_left_right_truncatable_prime(t):
    x = t[87]

    def is_left_right_truncatable_prime(n):
        if n < 2 or n == 4 or n == 6 or (n == 8) or (n == 9):
            return False
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            if not is_prime(int(s)):
                return False
            s = s[1:]
            s = s[:-1]
        return True

    def is_prime(n):
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
    return sorted([p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)])