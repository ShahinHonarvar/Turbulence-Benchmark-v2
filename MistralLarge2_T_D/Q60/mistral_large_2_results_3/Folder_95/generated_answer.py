def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    if not is_prime(n):
        return False
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[77]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(result)