def prime_factors(lst):
    number = lst[28]
    prime_factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return set(prime_factors)