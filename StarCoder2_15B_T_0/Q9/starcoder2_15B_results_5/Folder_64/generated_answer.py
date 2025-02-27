def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 0 to index 4, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints[0:5] if i % 2 != 0]