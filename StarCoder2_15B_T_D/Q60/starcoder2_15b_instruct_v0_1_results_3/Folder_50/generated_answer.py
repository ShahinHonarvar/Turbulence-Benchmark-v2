import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[0]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes