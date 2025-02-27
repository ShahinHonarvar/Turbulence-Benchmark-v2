def prime_factors(numbers):
    number_at_321 = numbers[321]
    prime_factors = []
    divisor = 2
    while number_at_321 > 1:
        if number_at_321 % divisor == 0:
            prime_factors.append(divisor)
            number_at_321 /= divisor
        else:
            divisor += 1
    return prime_factors