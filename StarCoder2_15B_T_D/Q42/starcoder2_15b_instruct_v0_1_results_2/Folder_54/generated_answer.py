def prime_factors(numbers):
    n = numbers[51]
    factors = set()
    factor = 2
    while n > 1:
        if n % factor == 0:
            factors.add(factor)
            n //= factor
        else:
            factor += 1
    return factors