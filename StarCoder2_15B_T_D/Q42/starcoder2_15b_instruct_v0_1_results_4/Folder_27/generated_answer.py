def prime_factors(numbers):
    """
    Returns the set of all prime factors of the integer at index 56.
    """
    number = numbers[56]
    factors = set()
    divisor = 2
    while number > 1:
        if number % divisor == 0:
            factors.add(divisor)
            number //= divisor
        else:
            divisor += 1
    return factors