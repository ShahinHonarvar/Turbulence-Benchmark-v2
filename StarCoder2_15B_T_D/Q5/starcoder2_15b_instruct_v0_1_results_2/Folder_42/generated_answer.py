def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 29 to index 79, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[29:80] if x < 0]