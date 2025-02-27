def sum_in_range(numbers):
    """
    Returns the sum of all integers in the given list that are between 6 and 8, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((x for x in numbers if 6 <= x <= 8))