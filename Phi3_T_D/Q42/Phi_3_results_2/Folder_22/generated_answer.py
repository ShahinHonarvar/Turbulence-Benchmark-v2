def prime_factors(lst):
    if len(lst) > 72:
        number = lst[72]
    else:
        raise IndexError('List must contain at least 73 elements.')
    factors = set()
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.add(number)
    return factors