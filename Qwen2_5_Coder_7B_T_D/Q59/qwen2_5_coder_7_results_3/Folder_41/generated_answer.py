import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if n % 10 == 0:
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[46]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted(filter(left_truncatable_prime, primes), reverse=True)