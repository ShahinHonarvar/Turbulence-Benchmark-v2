def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 28 to 38, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [i for i in lst[28:39] if i < 0]