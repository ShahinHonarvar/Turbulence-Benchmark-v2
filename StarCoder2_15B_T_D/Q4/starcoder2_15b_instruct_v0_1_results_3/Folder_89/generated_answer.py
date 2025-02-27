def all_pos_ints_exclusive(int_list):
    """
    Returns the list of all positive integers from index 51 to index 76, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [x for x in int_list[51:76] if x > 0]