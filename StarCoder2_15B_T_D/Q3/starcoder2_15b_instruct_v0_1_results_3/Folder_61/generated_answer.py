def all_pos_ints_inclusive(lst):
    """Returns the list of all positive integers from index 0 to index 7, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    return [x for x in lst if x > 0][0:8]