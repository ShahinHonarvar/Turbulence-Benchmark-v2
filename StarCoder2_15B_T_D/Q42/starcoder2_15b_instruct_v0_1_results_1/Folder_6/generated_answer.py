def prime_factors(numbers):
    n = numbers[790]
    factors = set()
    d = 2
    while n > 1:
        if n % d == 0:
            factors.add(d)
            n //= d
        else:
            d += 1
    return factors