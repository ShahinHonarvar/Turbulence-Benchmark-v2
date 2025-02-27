def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primes_in_range(n):
        return [x for x in range(2, n + 1) if is_prime(x)]

    def prime_factors_of_n(n, primes):
        factors = set()
        for prime in primes:
            while n % prime == 0:
                factors.add(prime)
                n //= prime
        return factors
    n = lst[91]
    primes = primes_in_range(n)
    return prime_factors_of_n(n, primes)