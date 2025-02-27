def prime_factors(numbers):
    number = numbers[321]
    prime_factors_set = set()
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            prime_factors_set.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return prime_factors_set