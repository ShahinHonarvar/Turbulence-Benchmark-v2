def prime_factors(numbers):
    number = numbers[4]
    prime_factors = []
    factor = 2
    while factor * factor <= number:
        while number % factor == 0:
            prime_factors.append(factor)
            number //= factor
        factor += 1
    if number > 1:
        prime_factors.append(number)
    return set(prime_factors)