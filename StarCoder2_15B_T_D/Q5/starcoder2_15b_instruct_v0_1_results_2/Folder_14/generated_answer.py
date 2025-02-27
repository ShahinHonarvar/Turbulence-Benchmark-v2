def all_neg_ints_inclusive(ints):
    """
    Returns the list of all negative integers from index 5 to index 7, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(5, 8):
        if ints[i] < 0:
            result.append(ints[i])
    return result