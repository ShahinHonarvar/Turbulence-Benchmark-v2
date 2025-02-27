def sum_in_range(lst):
    """
    Returns the sum of all integers from the given list that are between 7 and 9, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((x for x in lst if 7 <= x <= 9))