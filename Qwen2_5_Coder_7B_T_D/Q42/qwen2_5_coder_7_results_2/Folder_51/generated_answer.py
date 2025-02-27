def prime_factors(numbers):
    n = numbers[64]
    factors = set()
    divisor = 2
    while n >= 2:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    return factors