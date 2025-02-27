def prime_factors(numbers):
    number_at_index_247 = numbers[247]
    prime_factors = []
    divisor = 2
    while number_at_index_247 > 1:
        if number_at_index_247 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_247 //= divisor
        else:
            divisor += 1
    return set(prime_factors)