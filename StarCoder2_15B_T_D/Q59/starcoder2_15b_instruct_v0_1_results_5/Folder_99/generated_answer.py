def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    return is_left_truncatable(int(str(n)[1:]))

def all_left_truncatable_prime(x):
    return [n for n in range(2, x) if is_left_truncatable(n)]