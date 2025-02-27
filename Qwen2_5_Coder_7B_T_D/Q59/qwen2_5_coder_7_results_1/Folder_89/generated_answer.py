import sympy

def all_left_truncatable_prime(numbers):
    x = numbers[97]
    max_val = 10 ** 10
    primes = list(sympy.primerange(2, max_val))
    left_truncatable_primes = []
    for prime in primes:
        if all((int(prime[l:]) in primes for l in range(len(prime)))):
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)