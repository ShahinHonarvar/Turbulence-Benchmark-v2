def is_truncatable_prime(n):
    if n < 10:
        return False
    s = str(n)
    if '0' in s:
        return False
    for i in range(len(s) - 1):
        if not is_prime(int(s[i + 1:])):
            return False
        if not is_prime(int(s[:len(s) - i - 1])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[126]
    result = []
    for n in range(2, x + 1):
        if is_truncatable_prime(n):
            result.append(n)
    return sorted(result, reverse=True)