from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[0]
    result = []
    for i in range(1, x):
        s = str(i)
        is_left_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            result.append(i)
    return sorted(result, reverse=True)