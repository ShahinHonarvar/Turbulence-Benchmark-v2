def is_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
    return is_prime(n)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[29]
    result = []
    for i in range(2, x):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)