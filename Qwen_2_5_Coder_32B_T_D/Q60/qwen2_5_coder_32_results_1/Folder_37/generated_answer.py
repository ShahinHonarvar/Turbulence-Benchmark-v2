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
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[:i])) or not is_prime(int(s[i:])):
                return False
        return is_prime(int(s[:-1])) and is_prime(int(s[1:]))
    x = t[35]
    result = []
    for num in range(11, x + 1):
        if '0' not in str(num) and is_prime(num) and is_lr_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)