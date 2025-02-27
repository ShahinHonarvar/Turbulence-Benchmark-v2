def prime_factors(lst):
    p = 2
    factors = set()
    n = lst[926]
    while p * p <= n:
        if n % p:
            p += 1
        else:
            n //= p
            factors.add(p)
    if n > 1:
        factors.add(n)
    return factors