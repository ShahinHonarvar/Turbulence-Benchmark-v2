def prime_factors(numbers):
    number_at_index_95 = numbers[95]
    prime_factors = []
    divisor = 2
    while number_at_index_95 > 1:
        if number_at_index_95 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_95 //= divisor
        else:
            divisor += 1
    return set(prime_factors)