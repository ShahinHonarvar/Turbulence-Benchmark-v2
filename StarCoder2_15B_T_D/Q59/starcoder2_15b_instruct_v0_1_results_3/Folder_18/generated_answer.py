import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[429]
    left_truncatable_primes = []
    for i in range(1, x):
        n = i
        is_left_truncatable = True
        while n > 0:
            if not is_prime(n):
                is_left_truncatable = False
                break
            n //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)