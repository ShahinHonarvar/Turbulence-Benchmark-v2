def all_ints_not_div_by_num(lst):
    """
    Returns the list of all integers not divisible by 95 from index 20 to index 43, both exclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [x for i, x in enumerate(lst) if i >= 20 and i < 43 and (x % 95 != 0)]