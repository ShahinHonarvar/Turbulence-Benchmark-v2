def prime_factors(numbers):
    return set(prime_factors_of(numbers[49]))

def prime_factors_of(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d:
            d += 1
        else:
            n //= d
            factors.append(d)
    if n > 1:
        factors.append(n)
    return factors