def prime_factors(numbers):
    number = numbers[91]
    prime_factors = set()
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            prime_factors.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return prime_factors