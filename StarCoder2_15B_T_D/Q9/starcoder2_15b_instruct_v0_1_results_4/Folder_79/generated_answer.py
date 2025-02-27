def all_odd_ints_inclusive(ints_list):
    """
    Returns the list of all odd integers from index 4 to index 4, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for x in ints_list[4:5] if x % 2 != 0]