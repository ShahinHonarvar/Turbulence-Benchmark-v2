def prime_factors(num, primes=[2]):
    factors = set()
    for prime in primes:
        if prime > num:
            break
        while num % prime == 0:
            factors.add(prime)
            num //= prime
    if num > 1:
        return factors
    return None