from sympy import primerange, isprime

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not isprime(n) or n not in map(str, primes):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    primes = list(primerange(0, x + 1))
    left_truncatables = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return sorted(left_truncatables, reverse=True)