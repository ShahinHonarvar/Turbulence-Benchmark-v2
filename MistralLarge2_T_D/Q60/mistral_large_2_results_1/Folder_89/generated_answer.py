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

def is_left_right_truncatable(num):
    s = str(num)
    if '0' in s:
        return False
    if not is_prime(num):
        return False
    while len(s) > 1:
        s = s[1:-1]
        if not s or not is_prime(int(s)):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[97]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)