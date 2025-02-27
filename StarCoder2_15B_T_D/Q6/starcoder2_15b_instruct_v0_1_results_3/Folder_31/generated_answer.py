def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 87 to index 95, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [x for i, x in enumerate(lst) if i > 86 and i < 95 and (x < 0)]