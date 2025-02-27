import math

def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for n in range(2, x):
        is_left_truncatable = True
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes, reverse=True)

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