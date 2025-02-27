def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        if '0' in str(n) or not is_prime(n):
            return False
        l, r = (str(n), str(n))
        while len(l) > 2:
            l, r = (l[1:], r[:-1])
            if not is_prime(int(l)) or not is_prime(int(r)):
                return False
        return is_prime(int(l)) and is_prime(int(r))
    x = t[43]
    result = [n for n in range(10, x + 1) if is_lr_truncatable(n)]
    return result