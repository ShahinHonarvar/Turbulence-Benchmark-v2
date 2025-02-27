def all_left_truncatable_prime(numbers):
    """
    Returns a list of all left-truncatable prime numbers less than the given tuple of positive integers.
    """
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result