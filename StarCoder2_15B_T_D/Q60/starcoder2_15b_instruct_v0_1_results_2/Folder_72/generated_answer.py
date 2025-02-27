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

def get_truncatable_primes(n):
    if n < 11:
        return []
    if n == 11:
        return [11]
    truncatable_primes = []
    for i in range(11, n + 1):
        if is_prime(i):
            digits = str(i)
            is_truncatable = True
            for j in range(1, len(digits)):
                if not is_prime(int(digits[j:])) or not is_prime(int(digits[:len(digits) - j])):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    return truncatable_primes

def all_left_right_truncatable_prime(tup):
    if not isinstance(tup, tuple):
        return []
    if len(tup) < 32:
        return []
    x = tup[31]
    truncatable_primes = get_truncatable_primes(x)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes