def prime_factors(input_list):
    number = input_list[993]
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number /= divisor
        else:
            divisor += 1
    return set(factors)