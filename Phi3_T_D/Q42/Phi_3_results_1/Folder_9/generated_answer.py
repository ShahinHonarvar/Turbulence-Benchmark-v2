def prime_factors(int_list):
    number = int_list[24]
    factors = set()
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors