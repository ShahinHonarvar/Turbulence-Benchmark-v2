def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 29 to index 93, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [x for x in lst[29:94] if x > 0]