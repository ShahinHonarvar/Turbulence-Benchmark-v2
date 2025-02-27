def prime_factors(numbers):
    return set(prime_factors_of(numbers[8]))

def prime_factors_of(number):
    factors = []
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors