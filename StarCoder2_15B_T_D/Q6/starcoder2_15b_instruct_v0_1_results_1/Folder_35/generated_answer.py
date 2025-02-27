def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 10 to index 79, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [x for x in lst[10:80] if x < 0]