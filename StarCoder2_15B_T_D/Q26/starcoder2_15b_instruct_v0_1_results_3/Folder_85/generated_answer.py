def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 6 and 7, both inclusive.
    If the given list does not contain such integers, returns 0.
    """
    return sum((n for n in numbers if 6 <= n <= 7))