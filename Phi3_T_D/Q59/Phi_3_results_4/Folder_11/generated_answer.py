def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[86]
    result = []
    for n in range(2, x):
        if not is_left_truncatable(n) or '0' in str(n):
            continue
        result.append(n)
    return result