def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 661 to index 924, both inclusive.
    If no negative integers exist in the specified range, the function returns an empty list.
    """
    return [x for x in lst[661:925] if x < 0]