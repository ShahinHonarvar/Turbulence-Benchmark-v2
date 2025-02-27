def prime_factors(numbers):
    return set(prime_factors_of(numbers[63]))

def prime_factors_of(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors