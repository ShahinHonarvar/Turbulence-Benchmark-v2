def prime_factors(numbers):
    number_at_47 = numbers[47]
    prime_factors = set()
    divisor = 2
    while number_at_47 > 1:
        if number_at_47 % divisor == 0:
            prime_factors.add(divisor)
            number_at_47 //= divisor
        else:
            divisor += 1
    return prime_factors