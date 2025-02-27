def prime_factors(numbers):
    num_to_factor = numbers[51]
    factors = set()
    divisor = 2
    while num_to_factor > 1:
        while num_to_factor % divisor == 0:
            factors.add(divisor)
            num_to_factor //= divisor
        divisor += 1
    return factors