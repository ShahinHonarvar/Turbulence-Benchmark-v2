def all_pos_ints_exclusive(list_of_ints):
    """
    Returns a list of all positive integers from index 68 to index 99, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [i for i in list_of_ints[68:99] if i > 0]