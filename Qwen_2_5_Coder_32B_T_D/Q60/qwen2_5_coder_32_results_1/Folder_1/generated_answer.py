def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        sn = str(n)
        for i in range(len(sn)):
            if '0' in sn:
                return False
            if not (is_prime(int(sn[i:])) and is_prime(int(sn[:len(sn) - i]))):
                return False
        return True
    x = t[20]
    result = [n for n in range(2, x + 1) if is_lr_truncatable_prime(n)]
    return sorted(result, reverse=True)