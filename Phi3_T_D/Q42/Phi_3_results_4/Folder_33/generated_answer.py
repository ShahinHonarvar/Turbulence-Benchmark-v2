def prime_factors(num):
    factors = set()
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        factors.add(num)
    return factors