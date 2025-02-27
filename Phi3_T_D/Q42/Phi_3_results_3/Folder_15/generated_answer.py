def prime_factors(numbers_list):
    num_to_factor = numbers_list[10]
    factors = set()
    divisor = 2
    while divisor * divisor <= num_to_factor:
        while num_to_factor % divisor == 0:
            factors.add(divisor)
            num_to_factor //= divisor
        divisor += 1
    if num_to_factor > 1:
        factors.add(num_to_factor)
    return factors