import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for prime in numbers:
        if is_prime(prime):
            left_right_truncatable_primes.append(prime)
    return sorted(left_right_truncatable_primes, reverse=True)