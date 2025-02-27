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

def all_left_truncatable_prime(t):
    x = t[1]
    primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated = num
        while truncated and is_prime(truncated):
            truncated = int(str(truncated)[1:])
        if truncated == 0:
            primes.append(num)
    primes.sort(reverse=True)
    return primes