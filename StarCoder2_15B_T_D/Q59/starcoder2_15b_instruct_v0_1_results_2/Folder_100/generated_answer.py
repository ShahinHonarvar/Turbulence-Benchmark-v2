def all_left_truncatable_prime(t):
    x = t[26]

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def left_truncation(num):
        return int(str(num)[1:])
    res = []
    for i in range(x):
        num = i
        while num:
            if not is_left_truncatable_prime(num):
                break
            num = left_truncation(num)
        if not num:
            res.append(i)
    return sorted(res)