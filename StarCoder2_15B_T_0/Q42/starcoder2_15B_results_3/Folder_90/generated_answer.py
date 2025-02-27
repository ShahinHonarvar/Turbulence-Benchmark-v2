def prime_factors(numbers):
    number_at_index_263 = numbers[263]
    prime_factors = []
    divisor = 2
    while number_at_index_263 > 1:
        if number_at_index_263 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_263 //= divisor
        else:
            divisor += 1
    return set(prime_factors)