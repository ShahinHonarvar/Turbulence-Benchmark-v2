def prime_factors(numbers):
    number_at_index_94 = numbers[94]
    prime_factors = []
    divisor = 2
    while number_at_index_94 > 1:
        if number_at_index_94 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_94 //= divisor
        else:
            divisor += 1
    return set(prime_factors)