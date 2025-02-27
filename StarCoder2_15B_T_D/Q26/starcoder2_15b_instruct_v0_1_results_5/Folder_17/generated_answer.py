def sum_in_range(lst):
    """
    This function takes a list of integers and returns the sum of all integers
    between -816 and -166, both inclusive. If the given list does not contain
    such integers, the function returns 0.
    """
    return sum((x for x in lst if -816 <= x <= -166))