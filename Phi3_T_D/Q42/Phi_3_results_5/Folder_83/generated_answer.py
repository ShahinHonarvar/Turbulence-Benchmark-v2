def prime_factors(numbers):
    if len(numbers) > 95:
        num = numbers[95]
    else:
        num = 0
    if num <= 1:
        return set()
    factors = set()
    divisor = 2
    while divisor * divisor <= num:
        while num % divisor == 0:
            factors.add(divisor)
            num //= divisor
        divisor += 1
    if num > 1:
        factors.add(num)
    return factors