def prime_factors(numbers):
    number_at_90 = numbers[90]
    prime_factors = []
    divisor = 2
    while number_at_90 > 1:
        if number_at_90 % divisor == 0:
            prime_factors.append(divisor)
            number_at_90 //= divisor
        else:
            divisor += 1
    return set(prime_factors)