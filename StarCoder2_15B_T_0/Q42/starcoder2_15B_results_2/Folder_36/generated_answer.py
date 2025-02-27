def prime_factors(numbers):
    number_at_index_990 = numbers[990]
    prime_factors = []
    divisor = 2
    while number_at_index_990 > 1:
        if number_at_index_990 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_990 //= divisor
        else:
            divisor += 1
    return set(prime_factors)