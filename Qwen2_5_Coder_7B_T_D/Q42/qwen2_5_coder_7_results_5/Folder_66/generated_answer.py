def prime_factors(numbers):
    if len(numbers) <= 42:
        raise IndexError('List must contain at least 43 elements')
    number = numbers[42]
    factors = set()
    divisor = 2
    while number >= divisor * divisor:
        if number % divisor:
            divisor += 1
        else:
            number //= divisor
            factors.add(divisor)
    if number > 1:
        factors.add(number)
    return factors