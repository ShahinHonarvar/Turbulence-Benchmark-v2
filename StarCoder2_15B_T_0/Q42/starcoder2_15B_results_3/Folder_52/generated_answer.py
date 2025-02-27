def prime_factors(numbers):
    number_at_478 = numbers[478]
    prime_factors = []
    divisor = 2
    while number_at_478 > 1:
        if number_at_478 % divisor == 0:
            prime_factors.append(divisor)
            number_at_478 //= divisor
        else:
            divisor += 1
    return set(prime_factors)