def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 0 to index 1, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[0:1] if i % 2 != 0]