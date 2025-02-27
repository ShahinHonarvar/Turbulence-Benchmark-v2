def is_truncatable_prime(n):
    if n < 10:
        return False
    s = str(n)
    if '0' in s:
        return False
    while len(s) > 1:
        if not is_prime(int(s)):
            return False
        s = s[1:]
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    truncatable_primes = []
    for n in range(1, x + 1):
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
    return truncatable_primes