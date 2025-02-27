def all_left_right_truncatable_prime(t):
    x = t[54]
    left_truncated = [n for n in range(10, x + 1) if is_left_truncatable_prime(n)]
    right_truncated = [n for n in left_truncated if is_right_truncatable_prime(n)]
    return sorted(right_truncated, reverse=True)

def is_left_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return is_left_truncatable_prime(n // 10)

def is_right_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return is_right_truncatable_prime(n % 10)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True