def all_pos_ints_exclusive(integers_list):
    """
    Returns the list of all positive integers from index 81 to index 86, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [integer for integer in integers_list[81:86] if integer > 0]