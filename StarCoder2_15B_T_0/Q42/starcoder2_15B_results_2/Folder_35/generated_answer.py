def prime_factors(numbers):
    number_at_index_993 = numbers[993]
    prime_factors = []
    divisor = 2
    while number_at_index_993 > 1:
        if number_at_index_993 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_993 //= divisor
        else:
            divisor += 1
    return set(prime_factors)