from sympy import primerange, isprime

def is_left_truncatable_prime(p, primes_set):
    for i in range(len(str(p))):
        if not isprime(int(str(p)[:i + 1])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[945]
    truncatable_primes = []
    primes = set(primerange(2, x))
    for p in primes:
        if is_left_truncatable_prime(p, primes):
            truncatable_primes.insert(0, p)
    return truncatable_primes