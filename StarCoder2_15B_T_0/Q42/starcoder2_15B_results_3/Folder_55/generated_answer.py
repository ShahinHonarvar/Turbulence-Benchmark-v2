def prime_factors(numbers):
    number_at_21 = numbers[21]
    prime_factors = []
    divisor = 2
    while number_at_21 > 1:
        if number_at_21 % divisor == 0:
            prime_factors.append(divisor)
            number_at_21 //= divisor
        else:
            divisor += 1
    return set(prime_factors)