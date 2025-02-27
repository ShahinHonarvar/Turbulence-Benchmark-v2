def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 48 to index 76, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[48:76] if x < 0]