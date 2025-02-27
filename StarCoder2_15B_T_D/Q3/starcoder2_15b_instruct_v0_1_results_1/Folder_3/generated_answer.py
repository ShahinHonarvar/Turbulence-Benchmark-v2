def all_pos_ints_inclusive(my_list):
    """Returns the list of all positive integers from index 62 to index 92, both inclusive.
    If no positive integers exist in the specified range, returns an empty list."""
    return [x for x in my_list[62:93] if x > 0]