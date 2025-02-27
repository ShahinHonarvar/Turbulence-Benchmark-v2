def prime_factors(numbers):
    number_at_index_849 = numbers[849]
    prime_factors = set()
    divisor = 2
    while divisor <= number_at_index_849:
        while number_at_index_849 % divisor == 0:
            prime_factors.add(divisor)
            number_at_index_849 //= divisor
        divisor += 1
    return prime_factors