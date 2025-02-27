def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 3 and 8, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((n for n in numbers if 3 <= n <= 8))