def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 4 to 5, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for x in ints[4:6] if x % 2 != 0]