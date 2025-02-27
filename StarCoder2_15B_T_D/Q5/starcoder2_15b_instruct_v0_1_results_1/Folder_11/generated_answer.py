def all_neg_ints_inclusive(ints):
    """
    Returns a list of all negative integers from index 37 to 51, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[37:52] if i < 0]