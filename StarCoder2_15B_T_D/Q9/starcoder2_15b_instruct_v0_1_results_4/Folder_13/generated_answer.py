def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 25 to index 87, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[25:88] if i % 2 == 1]