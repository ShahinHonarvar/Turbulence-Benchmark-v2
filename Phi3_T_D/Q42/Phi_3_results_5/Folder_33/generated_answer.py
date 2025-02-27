def prime_factors(lst):
    if len(lst) <= 0 or not isinstance(lst[321], int) or lst[321] < 1:
        return set()

    def prime_factors_of(n):
        factors = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.add(d)
                n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return factors
    return prime_factors_of(lst[321])