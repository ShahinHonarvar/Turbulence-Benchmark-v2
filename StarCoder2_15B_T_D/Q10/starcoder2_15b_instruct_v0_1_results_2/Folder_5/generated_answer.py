def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers in the specified range from index 2 to index 7, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints[2:7] if i % 2 == 1]