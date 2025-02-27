import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n >= 10:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[78]
    return sorted([n for n in range(2, x) if right_truncatable_prime(n)], reverse=True)