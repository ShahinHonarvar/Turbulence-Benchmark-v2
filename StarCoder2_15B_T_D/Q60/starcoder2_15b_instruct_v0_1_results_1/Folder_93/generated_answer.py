import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    if n < 10:
        return [n] if is_prime(n) else []
    result = []
    for i in range(1, 10):
        if is_prime(n) and left_truncatable_primes(i):
            result.append(n)
    return result

def right_truncatable_primes(n):
    if n < 10:
        return [n] if is_prime(n) else []
    result = []
    for i in range(1, 10):
        if is_prime(n) and right_truncatable_primes(n % 10 ** (len(str(n)) - 1)):
            result.append(n)
    return result

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(10, x + 1):
        if left_truncatable_primes(i) and right_truncatable_primes(i):
            result.append(i)
    return result