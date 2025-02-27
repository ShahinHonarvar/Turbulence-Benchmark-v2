def prime_factors(numbers):
    number_at_33 = numbers[33]
    prime_factors = []
    divisor = 2
    while number_at_33 > 1:
        if number_at_33 % divisor == 0:
            prime_factors.append(divisor)
            number_at_33 //= divisor
        else:
            divisor += 1
    return set(prime_factors)