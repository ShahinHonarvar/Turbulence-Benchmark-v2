def prime_factors(lst):
    n = lst[247]
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
        if n > 1 and d >= 2:
            factors.add(n)
    return factors