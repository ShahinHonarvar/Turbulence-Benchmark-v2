def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 80 to index 200, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, val in enumerate(lst):
        if i >= 80 and i <= 200 and (val > 0):
            result.append(val)
    return result