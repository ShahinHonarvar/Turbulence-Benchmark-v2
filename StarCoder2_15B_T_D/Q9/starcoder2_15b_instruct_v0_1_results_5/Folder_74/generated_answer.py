def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 17 to index 78, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[17:79] if i % 2 == 1]