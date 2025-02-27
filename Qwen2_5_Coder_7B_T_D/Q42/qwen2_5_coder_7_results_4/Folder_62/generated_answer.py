def prime_factors(numbers):
    n = numbers[926]
    factors = set()
    divisor = 2
    while n >= divisor ** 2:
        if n % divisor:
            divisor += 1
        else:
            n //= divisor
            factors.add(divisor)
    if n > 1:
        factors.add(n)
    return factors