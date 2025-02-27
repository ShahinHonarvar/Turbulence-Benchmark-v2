def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 36 to index 52, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [x for i, x in enumerate(lst) if i >= 36 and i < 52 and (x < 0)]