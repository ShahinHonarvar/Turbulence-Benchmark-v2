def prime_factors(numbers):
    def_factors = []
    n = numbers[990]
    d = 2
    while d * d <= n:
        while n % d == 0:
            def_factors.append(d)
            n //= d
        d += 1
    if n > 1:
        def_factors.append(n)
    return set(def_factors)