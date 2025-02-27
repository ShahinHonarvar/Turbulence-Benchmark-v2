def all_pos_ints_exclusive(lst):
    """Returns the list of all positive integers from index 1 to index 7, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[1:7] if x > 0]