def all_ints_not_div_by_num(lst):
    """
    Returns the list of all integers not divisible by -17 from index 33 to index 78, both exclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [i for i in lst[33:78] if i % -17 != 0]