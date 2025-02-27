def all_pos_ints_exclusive(lst):
    """
    Returns a list of all positive integers from index 13 to index 76, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(lst):
        if 13 <= i < 76 and num > 0:
            result.append(num)
    return result