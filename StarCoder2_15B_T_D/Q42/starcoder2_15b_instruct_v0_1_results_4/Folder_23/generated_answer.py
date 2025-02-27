def prime_factors(numbers):
    number_at_index_69 = numbers[69]
    prime_factors = set()
    divisor = 2
    while divisor <= number_at_index_69:
        if number_at_index_69 % divisor == 0:
            prime_factors.add(divisor)
            number_at_index_69 //= divisor
        else:
            divisor += 1
    return prime_factors