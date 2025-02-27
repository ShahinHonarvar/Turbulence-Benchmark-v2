def is_right_truncatable_prime(n):
    if n < 2:
        return False
    while n >= 10:
        if is_prime(n):
            n //= 10
        else:
            return False
    return is_prime(n)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    return sorted([n for n in t if is_right_truncatable_prime(n)], reverse=True)