def prime_factors(numbers):
    number_at_42 = numbers[42]
    prime_factors = []
    divisor = 2
    while number_at_42 > 1:
        if number_at_42 % divisor == 0:
            prime_factors.append(divisor)
            number_at_42 //= divisor
        else:
            divisor += 1
    return set(prime_factors)