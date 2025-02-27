import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[0]

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        if n < 10:
            return True
        return is_left_truncatable_prime(int(str(n)[1:]))
    result = []
    for i in range(1, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)