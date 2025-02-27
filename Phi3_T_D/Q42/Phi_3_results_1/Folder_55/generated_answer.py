def prime_factors(numbers):
    num = numbers[21]
    factors = set()
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors