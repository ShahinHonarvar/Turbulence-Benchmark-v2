def all_ints_not_div_by_num(lst):
    """
    Returns the list of all integers not divisible by -53 from index 25 to index 76, both exclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(lst) if i >= 25 and i < 76 and (x % -53 != 0)]