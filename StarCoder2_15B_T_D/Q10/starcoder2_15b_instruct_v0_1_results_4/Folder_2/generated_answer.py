def all_odd_ints_exclusive(ints):
    """
    Returns a list of all odd integers from index 36 to index 52, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for x in ints[36:52] if x % 2 == 1]