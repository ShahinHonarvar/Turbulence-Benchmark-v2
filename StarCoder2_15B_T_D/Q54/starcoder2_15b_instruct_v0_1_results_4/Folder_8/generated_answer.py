import math

def all_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = [n for n in range(2, x) if is_prime(n)]
    right_truncatable_primes = [p for p in primes if is_right_truncatable(p)]
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    while n >= 10:
        n //= 10
        if not is_prime(n):
            return False
    return True