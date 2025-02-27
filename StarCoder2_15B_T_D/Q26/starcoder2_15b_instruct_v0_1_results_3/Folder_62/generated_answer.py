def sum_in_range(lst):
    """
    Write a function called'sum_in_range' that takes one argument, a list of integers, and returns the sum of all integers from the given list that are between -28 and 573, both inclusive. If the given list does not contain such integers, the function should return 0.
    """
    return sum((x for x in lst if -28 <= x <= 573))