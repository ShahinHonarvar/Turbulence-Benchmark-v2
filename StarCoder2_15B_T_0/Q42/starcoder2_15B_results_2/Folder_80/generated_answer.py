def prime_factors(numbers):
    number_at_index_746 = numbers[746]
    prime_factors = []
    divisor = 2
    while number_at_index_746 > 1:
        if number_at_index_746 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_746 //= divisor
        else:
            divisor += 1
    return set(prime_factors)