def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 75 to index 85, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[75:86] if x > 0]