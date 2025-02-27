import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[64]
    primes = [p for p in sympy.primerange(2, x) if '0' not in str(p)]
    left_truncatable_primes = [p for p in primes if all((sympy.isprime(int(str(p)[i:])) for i in range(len(str(p)))))]
    return sorted(left_truncatable_primes, reverse=True)