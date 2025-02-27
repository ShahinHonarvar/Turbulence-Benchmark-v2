def prime_factors(lst):
    n = lst[126]
    factors = set()
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    return factors