def all_ints_not_div_by_num(lst):
    """
    Returns the list of all integers not divisible by -78 from index 13 to index 70, both exclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(lst) if i >= 13 and i < 70 and (x % -78 != 0)]