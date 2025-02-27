def prime_factors(numbers):
    number_at_index_410 = numbers[410]
    prime_factors = []
    divisor = 2
    while number_at_index_410 > 1:
        if number_at_index_410 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_410 //= divisor
        else:
            divisor += 1
    return set(prime_factors)