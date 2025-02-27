def all_odd_ints_exclusive(ints):
    """
    Returns the list of all odd integers from index 10 to 11 (exclusive) in 'ints'.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(ints) if i >= 10 and i < 12 and (x % 2 == 1)]