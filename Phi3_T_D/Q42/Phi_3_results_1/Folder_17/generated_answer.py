def prime_factors(lst):

    def prime_factors_single(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors
    try:
        result = prime_factors_single(lst[632])
        return result
    except IndexError:
        return set()