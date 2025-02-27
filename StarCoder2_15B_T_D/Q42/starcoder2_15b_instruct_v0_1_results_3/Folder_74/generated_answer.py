def prime_factors(numbers):
    n = numbers[48]
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    return set(factors)