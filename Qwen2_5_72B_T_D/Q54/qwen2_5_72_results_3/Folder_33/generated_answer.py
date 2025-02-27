from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[945]
    right_truncatable_primes = [n for n in range(x - 1, 1, -1) if is_right_truncatable_prime(n)]
    return right_truncatable_primes