def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10 and n in [2, 3, 5, 7]:
        return True
    s = str(n)
    if '0' in s:
        return False
    left, right = (s, s)
    while len(left) > 1:
        left = left[1:]
        if not is_prime(int(left)):
            return False
    while len(right) > 1:
        right = right[:-1]
        if not is_prime(int(right)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[19]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)