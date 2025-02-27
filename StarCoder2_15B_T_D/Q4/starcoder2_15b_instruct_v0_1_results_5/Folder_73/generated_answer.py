def all_pos_ints_exclusive(lst):
    """
    Returns the list of all positive integers from index 36 to index 85, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(36, 85):
        if lst[i] > 0:
            result.append(lst[i])
    return result