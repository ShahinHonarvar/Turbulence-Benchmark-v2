def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list
    that are between 11 and 76, both inclusive. If the
    given list does not contain such integers, the function
    should return 0.
    """
    return sum((n for n in numbers if 11 <= n <= 76))