def prime_factors(numbers):
    number_at_702 = numbers[702]
    prime_factors = []
    divisor = 2
    while number_at_702 > 1:
        if number_at_702 % divisor == 0:
            prime_factors.append(divisor)
            number_at_702 //= divisor
        else:
            divisor += 1
    return set(prime_factors)