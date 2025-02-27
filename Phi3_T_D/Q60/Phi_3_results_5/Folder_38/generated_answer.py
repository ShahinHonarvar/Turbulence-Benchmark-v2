def is_prime(n):
    if n <= 1:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def is_left_right_truncatable_prime(n):
    if not (is_prime(n) and '0' not in str(n)):
        return False
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])):
            return False
        if not is_prime(int(n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[28]
    return sorted([p for p in range(2, x + 1) if is_left_right_truncatable_prime(p)])