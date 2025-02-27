def all_left_truncatable_prime(t):
    result = []
    x = t[98]
    if is_left_truncatable_prime(x):
        result.append(x)
    for i in range(1, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True