def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 36 to 46, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[36:47] if x < 0]