def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 75 to index 88, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [x for x in lst[75:90] if x < 0]