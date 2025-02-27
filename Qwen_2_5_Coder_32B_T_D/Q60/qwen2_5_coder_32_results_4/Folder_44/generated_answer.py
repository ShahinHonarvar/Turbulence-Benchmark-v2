def all_left_right_truncatable_prime(t):
    x = t[39]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            if not (is_prime(int(s)) and is_prime(int(s[::-1]))):
                return False
            s = s[1:-1]
        return True if is_prime(int(s)) else False
    return sorted([i for i in range(10, x + 1) if is_lr_truncatable_prime(i)])