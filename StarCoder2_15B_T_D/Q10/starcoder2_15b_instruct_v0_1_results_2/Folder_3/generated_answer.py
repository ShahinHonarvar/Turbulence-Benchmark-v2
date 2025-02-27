def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 78 to index 93, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(ints) if i >= 78 and i < 93 and (x % 2 == 1)]