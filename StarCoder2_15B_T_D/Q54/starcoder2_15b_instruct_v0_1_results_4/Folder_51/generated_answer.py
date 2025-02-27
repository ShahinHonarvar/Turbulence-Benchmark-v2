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

def all_right_truncatable_prime(t):
    x = t[54]
    right_truncatable_primes = []
    for i in range(x):
        n = i
        while n > 0:
            if not is_prime(n):
                break
            n //= 10
        if n == 0:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)