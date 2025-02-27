def prime_factors(numbers):
    number_at_index_63 = numbers[63]
    prime_factors = []
    divisor = 2
    while number_at_index_63 > 1:
        if number_at_index_63 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_63 //= divisor
        else:
            divisor += 1
    return set(prime_factors)