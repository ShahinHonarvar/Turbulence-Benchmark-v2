def right_truncatable_prime(n):
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

def all_right_truncatable_prime(tup):
    x = tup[26]
    result = []
    for i in range(2, x):
        if right_truncatable_prime(i):
            result.append(i)
    result.sort()
    return result