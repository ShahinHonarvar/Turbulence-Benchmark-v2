def sum_in_range(lst):
    """
    Return the sum of all integers in the specified range [-91, -41].

    Parameters:
    lst (list): A list of integers.

    Returns:
    int: The sum of integers between -91 and -41, both inclusive.
         0 if there are no such integers in the list.
    """
    return sum((x for x in lst if -91 <= x <= -41))