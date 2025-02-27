def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        s = s[1:-1]
        if not is_prime(int(s)):
            return False
    return is_prime(int(s))

def all_left_right_truncatable_prime(t):
    x = t[96]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)