from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[0]
    if x <= 760:
        return []
    result = []
    for i in range(760, x):
        temp = i
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            result.append(i)
    return sorted(result, reverse=True)