def sum_in_range(lst):
    """
    Returns the sum of all integers from the given list that are between 44 and 67, both inclusive.
    If the given list does not contain such integers, returns 0.
    """
    return sum((x for x in lst if 44 <= x <= 67))