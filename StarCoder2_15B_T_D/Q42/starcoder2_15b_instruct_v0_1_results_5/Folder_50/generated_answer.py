def prime_factors(lst):
    num = lst[40]
    factors = []
    factor = 2
    while num > 1:
        if num % factor == 0:
            factors.append(factor)
            num //= factor
        else:
            factor += 1
    return set(factors)