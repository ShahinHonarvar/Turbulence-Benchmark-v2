def prime_factors(numbers):
    if len(numbers) <= 34:
        return 'Index out of range'
    num = numbers[34]
    factors = set()
    divisor = 2
    while num >= divisor * divisor:
        if num % divisor:
            divisor += 1
        else:
            factors.add(divisor)
            num //= divisor
    if num > 1:
        factors.add(num)
    return factors