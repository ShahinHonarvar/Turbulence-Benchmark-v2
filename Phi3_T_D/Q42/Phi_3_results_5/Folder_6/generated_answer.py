def prime_factors(numbers):
    num_to_factor = numbers[790]
    factors = set()
    divisor = 2
    while divisor * divisor <= num_to_factor:
        if num_to_factor % divisor:
            divisor += 1
        else:
            num_to_factor //= divisor
            factors.add(divisor)
    if num_to_factor > 1:
        factors.add(num_to_factor)
    return factors