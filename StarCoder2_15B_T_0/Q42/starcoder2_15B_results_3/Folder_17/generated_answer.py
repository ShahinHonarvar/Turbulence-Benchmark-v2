def prime_factors(numbers):
    number_at_index_632 = numbers[632]
    prime_factors = []
    divisor = 2
    while number_at_index_632 > 1:
        if number_at_index_632 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_632 //= divisor
        else:
            divisor += 1
    return set(prime_factors)