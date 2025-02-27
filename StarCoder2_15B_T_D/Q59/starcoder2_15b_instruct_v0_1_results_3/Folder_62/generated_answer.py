def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[0]
    left_truncatable_primes = []
    for i in range(1, x):
        if is_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)