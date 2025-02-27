def prime_factors(numbers):
    if len(numbers) <= 41:
        return set()
    num = numbers[41]
    factors = set()
    divisor = 2
    while num >= divisor * divisor:
        if num % divisor:
            divisor += 1
        else:
            num //= divisor
            factors.add(divisor)
    if num > 1:
        factors.add(num)
    return factors