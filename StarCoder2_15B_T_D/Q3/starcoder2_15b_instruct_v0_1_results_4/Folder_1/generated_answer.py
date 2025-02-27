def all_pos_ints_inclusive(my_list):
    """
    Returns the list of all positive integers from index 31 to index 72, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(my_list) if 31 <= i <= 72 and x > 0]