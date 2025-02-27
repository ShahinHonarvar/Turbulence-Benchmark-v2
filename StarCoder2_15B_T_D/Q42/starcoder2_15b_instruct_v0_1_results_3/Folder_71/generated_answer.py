def prime_factors(lst):
    num = lst[78]
    factors = set()
    factor = 2
    while num > 1:
        if num % factor == 0:
            factors.add(factor)
            num //= factor
        else:
            factor += 1
    return factors