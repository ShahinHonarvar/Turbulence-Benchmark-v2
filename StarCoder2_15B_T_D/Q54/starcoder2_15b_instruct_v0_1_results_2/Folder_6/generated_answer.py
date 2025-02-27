def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[74]
    res = []
    for i in range(2, x):
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        else:
            res.append(i)
    return sorted(res)