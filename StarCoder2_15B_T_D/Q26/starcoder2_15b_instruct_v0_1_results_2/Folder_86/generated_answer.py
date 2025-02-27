def sum_in_range(lst):
    """
    Returns the sum of all integers in the given list that are between 142 and 980, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((x for x in lst if 142 <= x <= 980))