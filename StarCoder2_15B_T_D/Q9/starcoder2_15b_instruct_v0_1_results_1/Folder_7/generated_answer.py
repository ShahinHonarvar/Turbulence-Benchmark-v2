def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 661 to index 924, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints[661:925] if i % 2 == 1]