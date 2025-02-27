from sympy import isprime

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not isprime(n):
            return False
        n = int(n / 10)
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[41]
    primes = set(range(2, x))
    for i in range(2, int(x ** 0.5) + 1):
        if i in primes:
            primes.difference_update(range(i * 2, x, i))
    left_truncatable_primes = []
    for prime in sorted(primes, reverse=True):
        if prime < 10 or is_left_truncatable_prime(prime, primes):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes