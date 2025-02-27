import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[38]
    right_truncatable_primes = []
    for i in range(2, x):
        num = i
        is_right_truncatable = True
        while num >= 10:
            if not is_prime(num):
                is_right_truncatable = False
                break
            num //= 10
        if is_right_truncatable and is_prime(num):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)