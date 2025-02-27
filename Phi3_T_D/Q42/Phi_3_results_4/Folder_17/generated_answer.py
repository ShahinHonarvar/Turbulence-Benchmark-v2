def prime_factors(numbers):
    num = numbers[632]
    factors = set()
    divisor = 2
    while num >= divisor:
        if num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        else:
            divisor += 1
    return factors