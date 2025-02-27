def prime_factors(numbers):
    number_at_46 = numbers[46]
    prime_factors = []
    factor = 2
    while factor <= number_at_46:
        if number_at_46 % factor == 0:
            prime_factors.append(factor)
            number_at_46 //= factor
        else:
            factor += 1
    return set(prime_factors)