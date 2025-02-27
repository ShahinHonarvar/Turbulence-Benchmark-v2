from itertools import takewhile
from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = [i for i in range(2, x) if isprime(i)]
    right_truncatable_primes = []
    for prime in primes:
        if all((isprime(int(str(prime)[:i])) for i in range(1, len(str(prime)) + 1))):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes, reverse=True)