def all_ints_not_div_by_num(lst):
    """
    Returns the list of all integers not divisible by 97 from index 19 to index 69, both exclusive.
    If no such integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[19:69] if x % 97 != 0]