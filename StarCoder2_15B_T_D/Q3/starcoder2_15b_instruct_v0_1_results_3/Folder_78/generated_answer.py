def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 43 to index 51, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(lst):
        if num > 0 and 43 <= i <= 51:
            result.append(num)
    return result