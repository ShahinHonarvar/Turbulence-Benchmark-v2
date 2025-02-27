def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(str(n)[1:]) if n > 0 else 0
    return True

def all_left_truncatable_prime(t):
    x = t[46]
    return sorted([p for p in range(2, x) if is_left_truncatable_prime(p)], reverse=True)