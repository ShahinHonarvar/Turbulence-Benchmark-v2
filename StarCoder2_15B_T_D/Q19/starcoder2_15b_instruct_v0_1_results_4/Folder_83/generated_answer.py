def all_ints_not_div_by_num(integers):
    """
    Returns the list of all integers not divisible by -31 from index 90 to index 200, both exclusive.
    If no such integers exist in the specified range, an empty list is returned.
    """
    return [x for x in integers[90:200] if x % -31 != 0]