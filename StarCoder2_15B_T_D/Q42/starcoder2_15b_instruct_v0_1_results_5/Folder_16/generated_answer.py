def prime_factors(numbers):
    number = numbers[162]
    factors = set()
    factor = 2
    while factor <= number:
        if number % factor == 0:
            factors.add(factor)
            number //= factor
        else:
            factor += 1
    return factors