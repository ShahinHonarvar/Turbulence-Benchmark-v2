def prime_factors(numbers):
    number_at_985 = numbers[985]
    prime_factors = []
    factor = 2
    while factor <= number_at_985:
        if number_at_985 % factor == 0:
            prime_factors.append(factor)
            number_at_985 /= factor
        else:
            factor += 1
    return set(prime_factors)