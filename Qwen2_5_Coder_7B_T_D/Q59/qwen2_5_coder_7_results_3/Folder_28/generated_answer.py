from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[19]
    primes = [i for i in range(2, x) if isprime(i)]
    left_truncatable_primes = [p for p in primes if str(p)[0] not in '0' and all((isprime(int(str(p)[:i])) for i in range(1, len(str(p)))))]
    return sorted(left_truncatable_primes)