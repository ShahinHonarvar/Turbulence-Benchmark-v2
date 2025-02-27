def prime_factors(numbers):
    number_at_537 = numbers[537]
    prime_factors = []
    divisor = 2
    while number_at_537 > 1:
        if number_at_537 % divisor == 0:
            prime_factors.append(divisor)
            number_at_537 //= divisor
        else:
            divisor += 1
    return set(prime_factors)