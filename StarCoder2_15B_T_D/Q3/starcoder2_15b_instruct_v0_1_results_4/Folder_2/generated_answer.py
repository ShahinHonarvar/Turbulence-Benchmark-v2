def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 15 to index 39, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[15:40] if x > 0]