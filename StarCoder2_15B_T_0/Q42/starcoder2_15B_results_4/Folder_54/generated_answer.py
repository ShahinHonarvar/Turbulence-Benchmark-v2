def prime_factors(numbers):
    number_at_51 = numbers[51]
    prime_factors = []
    divisor = 2
    while number_at_51 > 1:
        if number_at_51 % divisor == 0:
            prime_factors.append(divisor)
            number_at_51 //= divisor
        else:
            divisor += 1
    return set(prime_factors)