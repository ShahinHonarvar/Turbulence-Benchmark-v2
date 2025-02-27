def sum_in_range(lst):
    """
    Returns the sum of all integers from the given list that are between 8 and 9, both inclusive.
    If the given list does not contain such integers, returns 0.
    """
    return sum((x for x in lst if 8 <= x <= 9))