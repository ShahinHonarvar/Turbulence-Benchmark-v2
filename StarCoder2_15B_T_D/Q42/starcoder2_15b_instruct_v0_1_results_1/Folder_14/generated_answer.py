def prime_factors(numbers):
    number_at_index_17 = numbers[17]
    prime_factors = set()
    divisor = 2
    while number_at_index_17 > 1:
        if number_at_index_17 % divisor == 0:
            prime_factors.add(divisor)
            number_at_index_17 //= divisor
        else:
            divisor += 1
    return prime_factors