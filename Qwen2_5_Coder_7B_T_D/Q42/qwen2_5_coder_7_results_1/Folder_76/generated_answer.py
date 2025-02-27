def prime_factors(numbers):
    n = numbers[537]
    factors = set()
    d = 2
    while d * d <= n:
        if n % d:
            d += 1
        else:
            n //= d
            factors.add(d)
    if n > 1:
        factors.add(n)
    return factors