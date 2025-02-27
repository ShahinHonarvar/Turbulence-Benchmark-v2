from functools import reduce

def is_prime(n):
    if n <= 1:
        return False
    return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))

def is_left_truncatable(p, base=10):
    if not is_prime(p):
        return False
    while p > 0:
        if not is_prime(p):
            return False
        p = p // base
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[32]
    return sorted([p for p in range(2, x) if is_left_truncatable(p)])