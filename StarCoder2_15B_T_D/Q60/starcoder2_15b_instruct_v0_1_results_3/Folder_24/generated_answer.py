def all_left_right_truncatable_prime(t):
    x = t[65]

    def is_truncatable_prime(num):
        if num < 10:
            return is_prime(num)
        if num % 10 == 0 or not is_prime(num):
            return False
        return is_truncatable_prime(num // 10) and is_truncatable_prime(num % 10 ** (len(str(num)) - 1))

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    res = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    res.sort(reverse=True)
    return res