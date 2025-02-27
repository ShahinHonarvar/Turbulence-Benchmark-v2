def prime_factors(numbers):
    p = set()
    num = numbers[47]
    factor = 2
    while num > 1:
        while num % factor == 0:
            p.add(factor)
            num //= factor
        factor += 1
    return p