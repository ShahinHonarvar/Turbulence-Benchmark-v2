def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 42 to index 68, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[42:70] if x > 0]