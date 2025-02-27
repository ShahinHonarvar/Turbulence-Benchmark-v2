import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(x):
    if len(x) == 1:
        return [x]
    right_truncatable_primes = set()
    for digit in range(1, 10):
        number = int(str(x) + str(digit))
        if is_prime(number):
            right_truncatable_primes.update(all_right_truncatable_prime(number))
    return sorted(right_truncatable_primes, reverse=True)