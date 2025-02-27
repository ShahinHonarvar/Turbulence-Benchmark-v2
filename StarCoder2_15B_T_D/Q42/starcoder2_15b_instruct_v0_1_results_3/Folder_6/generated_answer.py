def prime_factors(numbers):
    number_to_check = numbers[790]
    prime_factors = set()
    factor = 2
    while factor * factor <= number_to_check:
        if number_to_check % factor == 0:
            prime_factors.add(factor)
            number_to_check //= factor
        else:
            factor += 1
    prime_factors.add(number_to_check)
    return prime_factors