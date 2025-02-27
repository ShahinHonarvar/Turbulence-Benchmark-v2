import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[81]

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        if n < 10:
            return True
        return is_left_truncatable_prime(n % 10 ** len(str(n)) - 1)
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n) and n % 10 != 0], reverse=True)