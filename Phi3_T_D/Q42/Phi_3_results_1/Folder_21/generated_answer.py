def prime_factors(numbers):
    if not numbers:
        return set()
    num_at_410 = numbers[410]
    factors = set()
    divisor = 2
    while num_at_410 > 1:
        while num_at_410 % divisor == 0:
            factors.add(divisor)
            num_at_410 //= divisor
        divisor += 1
    return factors