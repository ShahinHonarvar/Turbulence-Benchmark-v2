def prime_factors(numbers):
    number_at_53 = numbers[53]
    prime_factors = set()
    divisor = 2
    while number_at_53 >= divisor:
        if number_at_53 % divisor == 0:
            prime_factors.add(divisor)
            number_at_53 //= divisor
        else:
            divisor += 1
    return prime_factors