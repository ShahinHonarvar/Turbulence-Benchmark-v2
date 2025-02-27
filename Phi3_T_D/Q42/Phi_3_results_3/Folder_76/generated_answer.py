def prime_factors(numbers):
    num_to_factor = numbers[537]
    factors = set()
    divisor = 2
    while num_to_factor >= divisor:
        if num_to_factor % divisor == 0:
            factors.add(divisor)
            num_to_factor //= divisor
        else:
            divisor += 1
    return factors