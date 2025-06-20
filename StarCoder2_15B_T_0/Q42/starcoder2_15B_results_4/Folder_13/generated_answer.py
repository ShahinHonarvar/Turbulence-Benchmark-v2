def prime_factors(lst):
    n = lst[126]
    factors = []
    d = 2
    while n > 1:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    return set(factors)