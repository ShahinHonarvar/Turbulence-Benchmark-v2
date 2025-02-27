def all_ints_not_div_by_num(lst):
    """
    Returns the list of all integers not divisible by -36 from index 19 to index 49, both exclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    return [i for i in lst[19:49] if i % -36 != 0]