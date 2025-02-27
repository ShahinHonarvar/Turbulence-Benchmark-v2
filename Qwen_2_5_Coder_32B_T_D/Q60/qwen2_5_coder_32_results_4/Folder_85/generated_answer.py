def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        s = str(n)
        while len(s) > 2:
            if not is_prime(int(s)):
                return False
            s = s[1:-1]
        return is_prime(int(s))
    x = t[94]
    result = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' not in s and is_lr_truncatable_prime(num):
            result.append(num)
    return result