def all_neg_ints_exclusive(ints):
    """Returns the list of all negative integers from index 86 to index 99, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    filtered_ints = [i for i in ints if i < 0]
    return filtered_ints[86:99]