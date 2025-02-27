def prime_factors(numbers):
    number = numbers[459]
    prime_factors = set()
    factor = 2
    while factor <= number:
        while number % factor == 0:
            prime_factors.add(factor)
            number //= factor
        factor += 1
    return prime_factors