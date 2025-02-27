def prime_factors(numbers):
    number = numbers[2]
    prime_factors = set()
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            prime_factors.add(factor)
            number //= factor
        else:
            factor += 1
    prime_factors.add(number)
    return prime_factors