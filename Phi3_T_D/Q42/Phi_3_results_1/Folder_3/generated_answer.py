def prime_factors(lst):

    def get_prime_factors(n):
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
    try:
        n = lst[100]
        return get_prime_factors(n)
    except (IndexError, ValueError, TypeError):
        return set()