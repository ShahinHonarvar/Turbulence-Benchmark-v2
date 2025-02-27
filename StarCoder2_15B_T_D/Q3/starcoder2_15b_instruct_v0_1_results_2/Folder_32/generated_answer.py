def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 21 to index 97, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[21:98] if x > 0]