def prime_factors(numbers):
    """
    Returns the set of all prime factors of the integer at index 87.
    """
    number = numbers[87]
    for i in range(2, number + 1):
        while number % i == 0:
            number //= i
    return i