def all_pos_ints_inclusive(my_list):
    """Returns the list of all positive integers from index 28 to index 40, both inclusive.
    If no positive integers exist in the specified range, returns an empty list."""
    return [x for x in my_list[28:41] if x > 0]