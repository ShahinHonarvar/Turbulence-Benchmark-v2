def prime_factors(numbers):
    factors = set()
    n = numbers[0]
    divisor = 2
    while n >= 2:
        while n % divisor == 0:
            factors.add(divisor)
            n //= divisor
        divisor += 1
    return factors