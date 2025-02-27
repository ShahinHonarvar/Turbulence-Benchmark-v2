def is_prime(n):
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

def is_left_right_truncatable(n):
    if not is_prime(n):
        return False
    s = str(n)
    while len(s) > 1:
        s = s[1:]
        if not is_prime(int(s)):
            return False
        s = s[:-1]
        if not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable(n):
            result.append(n)
    return result