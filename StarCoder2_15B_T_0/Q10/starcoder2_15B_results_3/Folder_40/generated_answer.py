def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 0 to index 2, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[0:2] if i % 2 == 1]