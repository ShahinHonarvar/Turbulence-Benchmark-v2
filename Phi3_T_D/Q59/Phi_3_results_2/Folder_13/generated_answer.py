from sympy import primerange

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not primes[n]:
            return False
        n = n % 1000000000
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    primes = [False, False] + list(primerange(2, x))
    left_truncatable_primes = [p for p in primes if p < 10 and p > 1 and is_left_truncatable_prime(p, primes)]
    return left_truncatable_primes