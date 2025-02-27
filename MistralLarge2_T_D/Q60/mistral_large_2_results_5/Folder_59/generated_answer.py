def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n):
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return is_prime(int(s))

def all_left_right_truncatable_prime(tup):
    x = tup[84]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = [p for p in primes if is_left_right_truncatable(p)]
    return sorted(truncatable_primes, reverse=True)