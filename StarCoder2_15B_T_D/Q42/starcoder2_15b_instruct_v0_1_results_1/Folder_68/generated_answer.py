def prime_factors(numbers):
    """
    Given a list of integers, returns the set of all prime factors of the integer at index 3.
    """
    number = numbers[3]
    prime_factors = set()
    factor = 2
    while factor * factor <= number:
        while number % factor == 0:
            prime_factors.add(factor)
            number //= factor
        factor += 1
    if number > 1:
        prime_factors.add(number)
    return prime_factors