def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 5 to index 7, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [x for x in ints[5:8] if x % 2 == 1]