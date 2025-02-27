def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 20 to index 200, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints[20:201] if i % 2 == 1]