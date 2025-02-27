def prime_factors(integers):
    num = integers[63]
    factors = set()
    divisor = 2
    while num >= 2:
        if num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors