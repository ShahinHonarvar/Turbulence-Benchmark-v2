def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 19 to index 92, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [x for x in lst[19:93] if x < 0]