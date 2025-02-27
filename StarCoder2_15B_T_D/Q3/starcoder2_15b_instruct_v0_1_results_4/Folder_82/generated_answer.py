def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 20 to index 200, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[20:201] if x > 0]