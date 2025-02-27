def all_ints_not_div_by_num(ints, num):
    """
    Returns the list of all integers not divisible by `num` from index 0 to index 1, both exclusive.
    If no such integers exist, returns an empty list.
    """
    return [i for i in ints[0:1] if i % num != 0]