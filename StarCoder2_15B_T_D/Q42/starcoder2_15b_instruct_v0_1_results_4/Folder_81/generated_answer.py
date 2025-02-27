def prime_factors(numbers):
    number_at_index_20 = numbers[20]
    prime_factors = []
    divisor = 2
    while number_at_index_20 > 1:
        if number_at_index_20 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_20 /= divisor
        else:
            divisor += 1
    return set(prime_factors)