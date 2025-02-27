def prime_factors(numbers):
    number_at_index_69 = numbers[69]
    prime_factors = []
    divisor = 2
    while number_at_index_69 > 1:
        if number_at_index_69 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_69 //= divisor
        else:
            divisor += 1
    return set(prime_factors)