def all_neg_ints_exclusive(ints):
    """
    Returns the list of all negative integers from index 1 to index 7, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(ints[1:8]):
        if num < 0:
            result.append(num)
    return result