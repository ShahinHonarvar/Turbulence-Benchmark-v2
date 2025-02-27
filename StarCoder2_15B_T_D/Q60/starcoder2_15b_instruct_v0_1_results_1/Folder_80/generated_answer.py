import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[14]
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n >= 10:
        n = int(str(n)[1:])
        if not is_prime(n):
            return False
    return True