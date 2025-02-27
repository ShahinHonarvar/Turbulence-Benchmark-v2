def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 6 to index 6, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 6 <= i <= 6:
            result.append(num)
    return result