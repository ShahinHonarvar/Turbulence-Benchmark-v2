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

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    s = str(n)
    if '0' in s:
        return False
    left_trunc = s
    right_trunc = s
    while len(left_trunc) > 1 and len(right_trunc) > 1:
        left_trunc = left_trunc[1:]
        right_trunc = right_trunc[:-1]
        if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[370]
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)