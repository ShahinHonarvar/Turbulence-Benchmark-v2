def prime_factors(lst):
    n = lst[453]
    factors = set()
    divisor = 2
    while divsior * divisor <= n:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.add(n)
    return factors