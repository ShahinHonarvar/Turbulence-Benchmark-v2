def is_left_right_truncatable_prime(n):
    if n < 10:
        return False
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
        if not is_prime(int(s[:len(s) - i])):
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
    x = t[0]
    result = []
    for n in range(2, x + 1):
        if is_left_right_truncatable_prime(n):
            result.append(n)
    result.sort(reverse=True)
    return result