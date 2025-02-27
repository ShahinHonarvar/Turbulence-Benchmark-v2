def prime_factors(numbers):
    number = numbers[99]
    prime_factors = set()
    factor = 2
    while factor <= number:
        if number % factor == 0:
            prime_factors.add(factor)
            number //= factor
        else:
            factor += 1
    return prime_factors