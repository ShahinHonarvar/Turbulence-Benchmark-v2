def prime_factors(numbers):
    number_at_57 = numbers[57]
    prime_factors = []
    divisor = 2
    while number_at_57 > 1:
        if number_at_57 % divisor == 0:
            prime_factors.append(divisor)
            number_at_57 //= divisor
        else:
            divisor += 1
    return set(prime_factors)