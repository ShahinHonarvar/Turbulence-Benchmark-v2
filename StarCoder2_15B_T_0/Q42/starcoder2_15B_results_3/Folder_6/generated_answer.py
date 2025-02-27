def prime_factors(numbers):
    number_at_index_790 = numbers[790]
    prime_factors = []
    divisor = 2
    while number_at_index_790 > 1:
        if number_at_index_790 % divisor == 0:
            prime_factors.append(divisor)
            number_at_index_790 //= divisor
        else:
            divisor += 1
    return set(prime_factors)