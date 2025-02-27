def prime_factors(numbers):
    number_at_46 = numbers[46]
    prime_factors = []
    divisor = 2
    while number_at_46 > 1:
        if number_at_46 % divisor == 0:
            prime_factors.append(divisor)
            number_at_46 //= divisor
        else:
            divisor += 1
    return set(prime_factors)