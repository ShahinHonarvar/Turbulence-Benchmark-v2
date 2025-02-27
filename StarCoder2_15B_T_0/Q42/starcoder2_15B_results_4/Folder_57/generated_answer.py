def prime_factors(numbers):
    number_at_92 = numbers[92]
    prime_factors = []
    divisor = 2
    while number_at_92 > 1:
        if number_at_92 % divisor == 0:
            prime_factors.append(divisor)
            number_at_92 //= divisor
        else:
            divisor += 1
    return set(prime_factors)