def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_truncatable_prime(n // 10) and is_truncatable_prime(n % 10)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[88]
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)