def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 26 to index 52, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(lst) if i >= 26 and i <= 52 and (x < 0)]