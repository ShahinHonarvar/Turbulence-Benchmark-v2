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

def all_right_truncatable_prime(t):
    x = t[65]
    primes = []
    for i in range(2, x):
        num = i
        while num > 0 and is_prime(num):
            num //= 10
        if num == 0:
            primes.append(i)
    return sorted(primes, reverse=True)