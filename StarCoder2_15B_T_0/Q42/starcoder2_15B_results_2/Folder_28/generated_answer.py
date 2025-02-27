def prime_factors(numbers):
    number_at_37 = numbers[37]
    prime_factors = []
    divisor = 2
    while number_at_37 > 1:
        if number_at_37 % divisor == 0:
            prime_factors.append(divisor)
            number_at_37 //= divisor
        else:
            divisor += 1
    return set(prime_factors)