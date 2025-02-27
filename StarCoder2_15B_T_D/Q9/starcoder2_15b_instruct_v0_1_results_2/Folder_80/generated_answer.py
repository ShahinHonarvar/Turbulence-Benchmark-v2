def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 64 to index 66, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(ints) if i >= 64 and i <= 66 and (x % 2 == 1)]