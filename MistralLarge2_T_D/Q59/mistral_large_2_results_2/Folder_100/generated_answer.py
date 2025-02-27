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

def is_left_truncatable(n):
    while n > 0:
        if not is_prime(n) or '0' in str(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(t):
    x = t[26]
    primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)