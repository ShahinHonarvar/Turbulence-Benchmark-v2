def sum_in_range(numbers):
    """
    Returns the sum of all integers from the given list that are between 273 and 451, both inclusive.
    If the given list does not contain such integers, returns 0.
    """
    return sum((x for x in numbers if 273 <= x <= 451))