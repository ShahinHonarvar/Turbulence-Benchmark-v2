def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[14]
    res = []
    for i in range(2, x):
        num = i
        is_lt_prime = True
        while num > 0:
            if not is_prime(num):
                is_lt_prime = False
                break
            num //= 10
        if is_lt_prime:
            res.append(i)
    return sorted(res)