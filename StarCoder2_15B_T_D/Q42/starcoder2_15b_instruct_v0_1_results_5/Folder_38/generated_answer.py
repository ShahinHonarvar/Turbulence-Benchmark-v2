def prime_factors(numbers):
    number_at_38 = numbers[38]
    prime_factors = []
    divisor = 2
    while number_at_38 > 1:
        if number_at_38 % divisor == 0:
            prime_factors.append(divisor)
            number_at_38 /= divisor
        else:
            divisor += 1
    return set(prime_factors)