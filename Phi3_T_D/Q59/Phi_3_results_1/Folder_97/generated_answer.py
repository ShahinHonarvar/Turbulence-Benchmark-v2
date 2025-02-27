import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    primes_less_than_x = [p for p in range(2, x) if sympy.isprime(p)]
    left_truncatable_primes = []
    for prime in primes_less_than_x:
        prime_str = str(prime)
        if all((sympy.isprime(int(prime_str[i:])) for i in range(len(prime_str)))):
            left_truncatable_primes.append(prime)
    return left_truncatable_primes