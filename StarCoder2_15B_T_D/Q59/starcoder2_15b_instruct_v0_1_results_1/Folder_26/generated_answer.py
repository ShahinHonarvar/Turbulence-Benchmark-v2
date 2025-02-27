import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[81]
    left_truncatable_primes = []
    for i in range(1, x):
        num = i
        while num < x:
            if not is_prime(num):
                break
            num //= 10
        else:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)