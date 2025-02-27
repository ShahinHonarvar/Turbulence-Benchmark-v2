def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    s = str(n)
    while s:
        if not is_prime(int(s)):
            return False
        s = s[1:-1]
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[10]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)