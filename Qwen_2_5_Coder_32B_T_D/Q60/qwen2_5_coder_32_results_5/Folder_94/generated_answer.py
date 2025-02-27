def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 2:
            if not is_prime(int(s)) or not is_prime(int(s[:-1])):
                return False
            s = s[1:-1]
        return is_prime(int(s)) and is_prime(int(s[0]))
    x = numbers[43]
    result = [n for n in range(11, x + 1) if is_lr_truncatable_prime(n)]
    return result