def prime_factors(numbers):
    number_at_48 = numbers[48]
    prime_factors = set()
    factor = 2
    while number_at_48 > 1:
        while number_at_48 % factor == 0:
            prime_factors.add(factor)
            number_at_48 //= factor
        factor += 1
    return prime_factors