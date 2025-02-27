def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10 and n != 2 and (n != 3) and (n != 5) and (n != 7):
        return False
    if n >= 10:
        return is_left_truncatable_prime(int(str(n)[1:]))
    return True

def all_left_truncatable_prime(t):
    x = t[758]
    result = []
    for i in range(1, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)