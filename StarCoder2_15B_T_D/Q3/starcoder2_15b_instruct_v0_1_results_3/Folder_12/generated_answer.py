def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 14 to index 64, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [x for x in lst[14:65] if x > 0]