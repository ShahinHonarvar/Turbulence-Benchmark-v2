def prime_factors(numbers):
    number_at_index_60 = numbers[60]
    prime_factors = set()
    divisor = 2
    while number_at_index_60 > 1:
        if number_at_index_60 % divisor == 0:
            prime_factors.add(divisor)
            number_at_index_60 //= divisor
        else:
            divisor += 1
    return prime_factors