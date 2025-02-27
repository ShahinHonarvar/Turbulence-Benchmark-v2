def all_ints_not_div_by_num(ints, num=2):
    """
    Returns a list of all integers not divisible by `num` from index 1 to index 6, both exclusive.
    If no such integers exist, returns an empty list.
    """
    return [x for x in ints[1:6] if x % num != 0]