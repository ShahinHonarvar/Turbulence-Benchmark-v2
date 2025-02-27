def prime_factors(lst):

    def primes_up_to(n):
        sieve = [True] * (n + 1)
        for p in range(2, int(n ** 0.5) + 1):
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
        return [p for p in range(2, n + 1) if sieve[p]]

    def factorize(n, primes):
        factors = set()
        for p in primes:
            if p * p > n:
                break
            while n % p == 0:
                factors.add(p)
                n //= p
        if n > 1:
            factors.add(n)
        return factors
    primes = primes_up_to(lst[88])
    return factorize(lst[88], primes)