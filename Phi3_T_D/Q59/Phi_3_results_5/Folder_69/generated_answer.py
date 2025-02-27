def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_left(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(tup):
    x = tup[760]
    res = []
    for i in range(x - 1, 1, -1):
        if is_truncatable_left(i):
            res.append(i)
    return res