def all_pos_ints_exclusive(lst):
    """
    Returns the list of all positive integers from index 40 to index 200, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[40:200] if x > 0]