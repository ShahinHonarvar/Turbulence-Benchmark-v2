def all_odd_ints_inclusive(a_list):
    """
    Returns the list of all odd integers from index 0 to index 6, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [x for x in a_list if x % 2 != 0 and 0 <= x <= 6]