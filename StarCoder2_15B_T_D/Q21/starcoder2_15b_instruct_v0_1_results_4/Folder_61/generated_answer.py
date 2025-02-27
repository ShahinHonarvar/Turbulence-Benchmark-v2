def all_ints_div_by_num(lst):
    """
    This function takes a list of integers as input and returns a list of all integers
    divisible by 7 from index 0 to index 0, both inclusive. If no such integers exist,
    an empty list is returned.
    """
    return [num for i, num in enumerate(lst) if i >= 0 and i <= 0 and (num % 7 == 0)]