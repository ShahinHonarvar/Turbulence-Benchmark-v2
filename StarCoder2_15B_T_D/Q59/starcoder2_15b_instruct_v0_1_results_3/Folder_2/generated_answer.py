import math

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[618]
    return sorted([p for p in range(2, x) if is_prime(p) and all((is_prime(int(str(p)[i:])) for i in range(1, len(str(p)))))])