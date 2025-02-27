def all_pos_ints_exclusive(integers):
    """
    Returns the list of all positive integers from index 10 to index 79, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in range(10, 80):
        if integers[i] > 0:
            result.append(integers[i])
    return result