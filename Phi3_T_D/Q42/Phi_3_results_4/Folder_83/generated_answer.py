from math import sqrt

def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n, primes):
        factors = set()
        for prime in primes:
            while n % prime == 0:
                factors.add(prime)
                n //= prime
        return factors
    try:
        n = numbers[95]
        if n == 0:
            return set()
        primes = [p for p in range(2, n + 1) if is_prime(p)]
        return prime_factors_of(n, primes)
    except IndexError:
        return 'The list is not long enough.'