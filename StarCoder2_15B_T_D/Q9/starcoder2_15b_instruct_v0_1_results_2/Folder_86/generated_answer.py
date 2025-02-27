def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 31 to 34, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [i for i in ints[31:35] if i % 2 == 1]