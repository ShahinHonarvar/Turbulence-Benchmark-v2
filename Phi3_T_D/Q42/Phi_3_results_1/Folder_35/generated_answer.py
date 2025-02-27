def prime_factors(numbers):
    if len(numbers) < 1000:
        return 'Index 993 out of range'
    number = numbers[993]
    factors = set()
    divisor = 2
    while number >= divisor * divisor:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        factors.add(number)
    return factors