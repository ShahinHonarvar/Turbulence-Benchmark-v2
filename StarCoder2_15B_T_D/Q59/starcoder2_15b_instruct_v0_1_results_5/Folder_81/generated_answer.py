import functools

def all_left_truncatable_prime(numbers):
    primes = []
    for i in range(2, 10):
        left_truncatable_prime(primes, [i], numbers[98])
    return primes

def left_truncatable_prime(primes, digits, x):
    n = functools.reduce(lambda a, b: a * 10 + b, digits)
    if n < x and is_prime(n):
        primes.append(n)
        for i in range(1, 10):
            left_truncatable_prime(primes, digits + [i], x)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True