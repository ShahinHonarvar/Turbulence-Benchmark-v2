def all_neg_ints_exclusive(lst):
    """
    Returns the list of all negative integers from index 2 to index 8, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(2, 8):
        if lst[i] < 0:
            result.append(lst[i])
    return result