def prime_factors(numbers):
    number_at_43 = numbers[43]
    prime_factors = []
    divisor = 2
    while number_at_43 > 1:
        if number_at_43 % divisor == 0:
            prime_factors.append(divisor)
            number_at_43 /= divisor
        else:
            divisor += 1
    return set(prime_factors)