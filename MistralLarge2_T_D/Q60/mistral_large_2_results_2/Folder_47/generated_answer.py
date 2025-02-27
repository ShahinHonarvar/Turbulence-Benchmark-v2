def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    str_n = str(n)
    if '0' in str_n:
        return False
    left, right = (0, len(str_n) - 1)
    while left < right:
        if not is_prime(int(str_n[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[49]
    primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(primes)