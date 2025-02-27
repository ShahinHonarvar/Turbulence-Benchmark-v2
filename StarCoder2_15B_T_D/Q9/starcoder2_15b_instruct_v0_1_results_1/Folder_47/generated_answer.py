def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 37 to index 76, both inclusive,
    given a list of integers. If no odd integers exist in the specified range,
    an empty list is returned.
    """
    return [i for i in ints[37:77] if i % 2 != 0]