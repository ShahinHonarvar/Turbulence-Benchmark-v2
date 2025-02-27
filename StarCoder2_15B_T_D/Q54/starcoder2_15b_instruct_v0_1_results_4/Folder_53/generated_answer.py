import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    if len(str(x)) == 1:
        return [x] if is_prime(x) else []
    if is_prime(x):
        return [x] + all_right_truncatable_prime(int(str(x)[:-1]))
    return []