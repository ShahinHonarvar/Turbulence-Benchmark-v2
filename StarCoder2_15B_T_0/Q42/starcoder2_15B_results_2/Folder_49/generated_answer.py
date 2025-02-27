def prime_factors(numbers):
    number_at_index_68 = numbers[68]
    prime_factors = []
    divisor = 2
    while number_at_index_68 > 1:
        if number_at_index_68 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_68 //= divisor
        else:
            divisor += 1
    return set(prime_factors)