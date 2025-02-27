def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 38 to index 52, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [x for i, x in enumerate(ints) if i >= 38 and i < 52 and (x % 2 != 0)]