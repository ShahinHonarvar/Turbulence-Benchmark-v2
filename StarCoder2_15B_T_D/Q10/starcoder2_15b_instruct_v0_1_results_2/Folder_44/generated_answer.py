def all_odd_ints_exclusive(int_list):
    """
    Returns the list of all odd integers from index 81 to index 86, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for x in int_list[81:86] if x % 2 != 0]