def prime_factors(numbers):
    n = numbers[84]
    factors = set()
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    return factors