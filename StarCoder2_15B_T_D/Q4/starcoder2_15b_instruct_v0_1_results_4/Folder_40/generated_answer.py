def all_pos_ints_exclusive(ints):
    """
    Returns the list of all positive integers from index 0 to index 2, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(0, 2):
        if ints[i] > 0:
            result.append(ints[i])
    return result