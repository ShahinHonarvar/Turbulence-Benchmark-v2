def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return is_prime(int(s)) and is_prime(int(s[0])) and is_prime(int(s[-1]))
    x = t[20]
    result = [i for i in range(10, x + 1) if is_lr_truncatable(i)]
    return sorted(result, reverse=True)