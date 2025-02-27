def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        n //= 10
        if n == 0:
            return True
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[4]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_left_truncatable_prime(n):
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)