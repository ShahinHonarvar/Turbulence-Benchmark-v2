from math import sqrt

def prime_factors(numbers):
    if len(numbers) < 49 or not isinstance(numbers[48], int) or numbers[48] <= 1:
        return set()

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        primes = set()
        for i in range(2, n + 1):
            if is_prime(i):
                primes.add(i)
        return primes
    num = numbers[48]
    primes = get_primes(int(sqrt(num)) + 1)
    factors = set()
    for p in primes:
        while num % p == 0:
            factors.add(p)
            num //= p
    if num > 1:
        factors.add(num)
    return factors