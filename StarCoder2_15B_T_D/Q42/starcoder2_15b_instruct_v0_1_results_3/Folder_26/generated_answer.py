def prime_factors(numbers):
    number_at_222 = numbers[222]
    prime_factors = set()
    divisor = 2
    while divisor <= number_at_222:
        if number_at_222 % divisor == 0:
            number_at_222 //= divisor
            prime_factors.add(divisor)
        else:
            divisor += 1
    return prime_factors