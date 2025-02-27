def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 44 to index 91, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(lst) if i >= 44 and i < 91 and (num < 0)]