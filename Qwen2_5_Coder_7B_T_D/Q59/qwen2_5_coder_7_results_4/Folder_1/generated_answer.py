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

def left_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(t):
    x = t[20]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)