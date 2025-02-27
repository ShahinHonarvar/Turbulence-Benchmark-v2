def prime_factors(numbers):
    number_at_index_93 = numbers[93]
    prime_factors = []
    divisor = 2
    while number_at_index_93 > 1:
        if number_at_index_93 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_93 //= divisor
        else:
            divisor += 1
    return set(prime_factors)