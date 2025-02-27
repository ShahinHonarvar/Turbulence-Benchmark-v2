def prime_factors(numbers):
    number_at_74 = numbers[74]
    prime_factors = set()
    divisor = 2
    while number_at_74 > 1:
        if number_at_74 % divisor == 0:
            prime_factors.add(divisor)
            number_at_74 //= divisor
        else:
            divisor += 1
    return prime_factors