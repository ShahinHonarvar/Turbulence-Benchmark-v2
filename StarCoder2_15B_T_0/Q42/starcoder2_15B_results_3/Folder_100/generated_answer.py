def prime_factors(numbers):
    number_at_index_99 = numbers[99]
    prime_factors = []
    divisor = 2
    while number_at_index_99 > 1:
        if number_at_index_99 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_99 //= divisor
        else:
            divisor += 1
    return set(prime_factors)