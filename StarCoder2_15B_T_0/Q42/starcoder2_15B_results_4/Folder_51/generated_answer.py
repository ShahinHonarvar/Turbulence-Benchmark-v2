def prime_factors(numbers):
    number_at_index_64 = numbers[64]
    prime_factors = []
    divisor = 2
    while number_at_index_64 > 1:
        if number_at_index_64 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_64 //= divisor
        else:
            divisor += 1
    return set(prime_factors)