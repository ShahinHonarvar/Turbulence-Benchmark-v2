def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 0 to index 3, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints[0:3] if i % 2 == 1]