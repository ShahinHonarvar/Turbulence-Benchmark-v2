def prime_factors(numbers):
    if len(numbers) <= 40:
        return 'List is too short'
    num = numbers[40]
    factors = set()
    divisor = 2
    while num >= 2:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    return factors