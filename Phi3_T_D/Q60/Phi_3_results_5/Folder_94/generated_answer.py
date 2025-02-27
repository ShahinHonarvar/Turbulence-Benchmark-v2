def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n, seg=(), seen=None):
    if seen is None:
        seen = set()
    if n in seen:
        return False
    seen.add(n)
    s = str(n)
    while s:
        num = int(s)
        if num > 10 and (not is_left_right_truncatable_prime(num, seg + (n % 10,), seen)):
            return False
        s = s[:-1]
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    return sorted([n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)])