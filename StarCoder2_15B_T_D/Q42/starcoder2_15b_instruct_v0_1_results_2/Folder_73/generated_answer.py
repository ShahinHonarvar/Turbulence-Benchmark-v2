def prime_factors(numbers):
    number_at_41 = numbers[41]
    prime_factors = set()
    factor = 2
    while factor * factor <= number_at_41:
        while number_at_41 % factor == 0:
            prime_factors.add(factor)
            number_at_41 //= factor
        factor += 1
    if number_at_41 > 1:
        prime_factors.add(number_at_41)
    return prime_factors