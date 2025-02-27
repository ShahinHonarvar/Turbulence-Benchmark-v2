def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 87 to index 95, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[87:95] if x < 0]