def sum_in_range(nums):
    """
    Returns the sum of all integers from the given list that are between 13 and 35, both inclusive.
    If the given list does not contain such integers, the function returns 0.
    """
    return sum((x for x in nums if 13 <= x <= 35))